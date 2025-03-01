# crud.py
from typing import Dict, List
import json
from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from .models import User, Doctor, Appointment, ChatHistory
from datetime import datetime, timedelta
from .utils import get_weekday, call_dify_api  # 导入工具函数



# 密码加密器
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# 用户注册
def create_user(db: Session, email: str, fullname: str, password: str):
    hashed_password = pwd_context.hash(password)
    db_user = User(email=email, fullname=fullname, password_hash=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# 获取用户
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


# 验证密码
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


# 获取用户的聊天历史
def get_chat_history(db: Session, user_id: int):
    return db.query(ChatHistory).filter(ChatHistory.user_id == user_id).all()

# 存储用户的聊天消息
def store_user_message(db: Session, message: dict) -> ChatHistory:
    db_message = ChatHistory(
        user_id=message["user_id"],
        conversation_id=message["conversation_id"],
        message=message["message"],
        is_user=message["is_user"],
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

# 存储机器人的回复消息
def store_bot_message(db: Session, bot_response: dict, user_id: int) -> ChatHistory:
    db_message_bot = ChatHistory(
        user_id=user_id,
        conversation_id=bot_response["conversation_id"],
        message=bot_response["answer"],
        is_user=False,
    )

    # 添加空值检查
    if not db_message_bot.message:
        db_message_bot.message = "sorry, i can't answer it"

    db.add(db_message_bot)
    db.commit()
    db.refresh(db_message_bot)
    return db_message_bot


# 获取医生列表
def get_doctors(db: Session):
    return db.query(Doctor).all()


# # 获取用户预约记录
# def get_user_appointments(db: Session, user_id: int):
#     appointments = db.query(Appointment).filter(Appointment.user_id == user_id).all()
#     doctor_ids = set(appointment.doctor_id for appointment in appointments)

#     doctor_map = {}
#     if doctor_ids:
#         doctors = db.query(Doctor).filter(Doctor.doctor_id.in_(doctor_ids)).all()
#         doctor_map = {doctor.doctor_id: doctor.name for doctor in doctors}

#     return [
#         {
#             "appointment_id": appointment.appointment_id,
#             "doctor_name": doctor_map.get(appointment.doctor_id, "未知医生"),
#             "appointment_date": appointment.appointment_date,
#             "status": appointment.status,
#             "notes": appointment.notes
#         }
#         for appointment in appointments
#     ]
# 获取用户预约记录
def get_user_appointments(db: Session, user_id: int):
    # 获取当前时间
    current_time = datetime.now()
    
    # 只获取当前时间之后的预约
    appointments = db.query(Appointment).filter(
        Appointment.user_id == user_id,
        Appointment.appointment_date > current_time
    ).order_by(Appointment.appointment_date.asc()).all()
    
    doctor_ids = set(appointment.doctor_id for appointment in appointments)

    doctor_map = {}
    if doctor_ids:
        doctors = db.query(Doctor).filter(Doctor.doctor_id.in_(doctor_ids)).all()
        doctor_map = {doctor.doctor_id: doctor.name for doctor in doctors}

    return [
        {
            "appointment_id": appointment.appointment_id,
            "doctor_name": doctor_map.get(appointment.doctor_id, "Unknown Doctor"),
            "appointment_date": appointment.appointment_date,
            "status": appointment.status,
            "notes": appointment.notes
        }
        for appointment in appointments
    ]

# # 获取医生的可用时间
# def get_doctor_availability(db: Session, doctor_id: int, weekday: str):
#     doctor = db.query(Doctor).filter(Doctor.doctor_id == doctor_id).first()
#     if doctor:
#         return doctor.availability
#     return None
# 获取医生的可用时间并检查每个时间段是否有预约
def get_doctor_availability(db: Session, doctor_id: int, queryTime: str) -> List[Dict]:
    # 先转换 queryTime 为星期
    weekday = get_weekday(queryTime)

    # 获取医生信息
    doctor = db.query(Doctor).filter(Doctor.doctor_id == doctor_id).first()

    if not doctor or not doctor.availability:
        return []

    # 获取医生的可用时间
    availability_str = json.loads(json.dumps(doctor.availability)).get(weekday)
    if not availability_str:
        return []

    # 解析可用时间字符串，如 "9:00-17:00"
    start_time_str, end_time_str = availability_str.split('-')

    # 转换时间字符串为 datetime 对象
    start_time = datetime.strptime(start_time_str, "%H:%M")
    end_time = datetime.strptime(end_time_str, "%H:%M")

    # 生成小时时间段列表
    time_slots = []
    current_time = start_time
    while current_time < end_time:
        time_slots.append(current_time.strftime("%H:%M"))
        current_time += timedelta(hours=1)

    # 将 queryTime 转换为 datetime 对象
    query_date = datetime.strptime(queryTime, "%Y-%m-%d").date()

    # 查询指定日期的预约记录
    available_slots = []
    for slot in time_slots:
        # 将时间和 queryTime 的日期拼接，生成完整的时间戳
        appointment_time = datetime.strptime(f"{query_date} {slot}", "%Y-%m-%d %H:%M")

        # 检查是否有预约记录
        appointment = db.query(Appointment).filter(
            Appointment.doctor_id == doctor_id,
            Appointment.appointment_date == appointment_time
        ).first()

        # 如果该时间段没有预约，设置为可用
        if appointment is None:
            available_slots.append({
                "time": slot,
                "available": True
            })
        else:
            # 如果有预约，设置为不可用
            available_slots.append({
                "time": slot,
                "available": False
            })

    return available_slots


# 创建预约
def create_appointment(db: Session, user_id: int, doctor_id: int, appointment_date: datetime, status: str, notes: str):
    # 检查医生是否存在
    doctor = db.query(Doctor).filter(Doctor.doctor_id == doctor_id).first()
    if not doctor:
        return None

    # # 检查用户是否已有未完成的预约
    # existing_appointment = db.query(Appointment).filter(Appointment.user_id == user_id,
    #                                                     Appointment.status == "scheduled").first()
    # if existing_appointment:
    #     raise HTTPException(status_code=400, detail="用户有未完成的预约")

    # 检查用户是否已有未完成的预约（只检查未来的预约）
    current_time = datetime.now()
    existing_appointment = db.query(Appointment).filter(
        Appointment.user_id == user_id,
        Appointment.status == "scheduled",
        Appointment.appointment_date > current_time
    ).first()
    
    if existing_appointment:
        raise HTTPException(status_code=400, detail="The user has unfinished appointments")


    # 检查该医生是否在该时间已被预约
    already_booked = db.query(Appointment).filter(
        Appointment.doctor_id == doctor_id,
        Appointment.appointment_date == appointment_date
    ).first()
    if already_booked:
        raise HTTPException(status_code=400, detail="The doctor has already been scheduled at that time")

    new_appointment = Appointment(
        user_id=user_id,
        doctor_id=doctor_id,
        appointment_date=appointment_date,
        status=status,
        notes=notes
    )
    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)

    return new_appointment

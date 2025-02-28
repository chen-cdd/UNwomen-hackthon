# main.py

import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import get_chat_history, get_doctors, get_user_appointments, get_doctor_availability, create_appointment, store_user_message, store_bot_message
from models import User, Doctor, Appointment, ChatHistory
from schemas import ChatHistoryResponse, CreateChatMessage, DoctorResponse, AppointmentResponse, AppointmentCreate
from database import SessionLocal
from utils import call_dify_api  # 导入工具函数

# 初始化 FastAPI 应用
app = FastAPI()


# 获取数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 1. 获取用户的聊天历史
@app.get("/api/chat/history", response_model=List[ChatHistoryResponse])
def get_chat_history_endpoint(user_id: int, db: Session = Depends(get_db)):
    # 返回响应
    return {
        "success": True,
        "data": get_chat_history(db, user_id)
    }


# 2. 发送一条聊天消息
@app.post("/api/chat/message", response_model=dict)
def create_chat_message(message: CreateChatMessage, db: Session = Depends(get_db)):
    # 1. 存储用户的消息
    user_message = store_user_message(db, message.dict())

    payload = {
        "inputs": {},
        "query": message.message,
        "response_mode": "blocking",
        "conversation_id": message.conversation_id,
        "user": message.user_id,
        "files": []
    }

    # 2. 调用 DIFY API 获取机器人的回复
    bot_response = call_dify_api(payload)

    # 3. 存储机器人的消息
    bot_message = store_bot_message(db, bot_response, message.user_id)

    # 返回响应
    return {
        "success": True,
        "response": bot_response,
        "chat_id": user_message.chat_id  # 使用用户消息的 chat_id
    }


# 3. 获取医生列表
@app.get("/api/doctors", response_model=List[DoctorResponse])
def get_doctors_endpoint(db: Session = Depends(get_db)):
    # 返回响应
    return {
        "success": True,
        "data": get_doctors(db)
    }


# 4. 获取用户预约记录
@app.get("/api/appointments/user/{user_id}", response_model=List[AppointmentResponse])
def get_user_appointments_endpoint(user_id: int, db: Session = Depends(get_db)):
    # 返回响应
    return {
        "success": True,
        "data": get_user_appointments(db, user_id)
    }


# 5. 获取医生的可用时间
@app.get("/api/doctors/{doctor_id}/availability", response_model=dict)
def get_doctor_availability_endpoint(doctor_id: int, queryTime: str, db: Session = Depends(get_db)):


    # 调用 get_doctor_availability 函数，传递星期信息
    availability = get_doctor_availability(db, doctor_id, queryTime)

    if not availability:
        raise HTTPException(status_code=404, detail="Doctor not found")

    return {"success": True, "data": availability}


# 6. 创建预约
@app.post("/api/appointments", response_model=dict)
def create_appointment_endpoint(appointment: AppointmentCreate, db: Session = Depends(get_db)):
    new_appointment = create_appointment(
        db,
        appointment.user_id,
        appointment.doctor_id,
        appointment.appointment_date,
        appointment.status,
        appointment.notes
    )
    if not new_appointment:
        raise HTTPException(status_code=400, detail="无法创建预约")

    doctor = db.query(Doctor).filter(Doctor.doctor_id == appointment.doctor_id).first()
    return {
        "success": True,
        "data": {
            "appointment_id": new_appointment.appointment_id,
            "doctor_name": doctor.name,
            "appointment_date": new_appointment.appointment_date,
            "status": new_appointment.status
        },
        "message": "预约成功"
    }


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1")

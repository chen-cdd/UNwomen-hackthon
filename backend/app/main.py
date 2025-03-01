# main.py

import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Dict

from .crud import get_chat_history, get_doctors, get_user_appointments, get_doctor_availability, create_appointment, store_user_message, store_bot_message, get_user_by_email, verify_password, create_user
from .models import User, Doctor, Appointment, ChatHistory
from .schemas import  LoginRequest, RegisterRequest, ChatHistoryDataResponse, CreateChatMessage, DoctorDataResponse, AppointmentDataResponse, AppointmentCreate
from .database import SessionLocal
from .utils import call_dify_api  # 导入工具函数
from fastapi.middleware.cors import CORSMiddleware  # 添加这行导入

# 初始化 FastAPI 应用
app = FastAPI()

# 添加 CORS 中间件配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # 允许的前端域名
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有 HTTP 方法
    allow_headers=["*"],  # 允许所有 headers
)

# 获取数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 登录接口
@app.post("/api/auth/login", response_model=dict)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = get_user_by_email(db, request.email)
    if not user or not verify_password(request.password, user.password_hash):
        raise HTTPException(status_code=400, detail="邮箱或密码错误")

    return {
        "success": True,
        "user": {"user_id": user.user_id, "email": user.email},
        "message": "登录成功"
    }


# 注册接口
@app.post("/api/auth/register", response_model=dict)
def register(request: RegisterRequest, db: Session = Depends(get_db)):
    # 检查邮箱是否已注册
    user = get_user_by_email(db, request.email)
    if user:
        raise HTTPException(status_code=400, detail="该邮箱已被注册")

    new_user = create_user(db, request.email, request.fullname, request.password)
    return {
        "success": True,
        "user": {"user_id": new_user.user_id, "email": new_user.email, "fullname": new_user.fullname},
        "message": "注册成功"
    }

# 1. 获取用户的聊天历史
@app.get("/api/chat/history", response_model=ChatHistoryDataResponse)
def get_chat_history_endpoint(user_id: int, db: Session = Depends(get_db)):
    chat_history = get_chat_history(db, user_id)

    return {
        "success": True,
        "data": chat_history,
    }


# # 2. 发送一条聊天消息
# @app.post("/api/chat/message", response_model=dict)
# def create_chat_message(message: CreateChatMessage, db: Session = Depends(get_db)):
#     # 1. 存储用户的消息
#     user_message = store_user_message(db, message.dict())

#     payload = {
#         "inputs": {},
#         "query": message.message,
#         "response_mode": "blocking",
#         "conversation_id": message.conversation_id,
#         "user": message.user_id,
#         "files": []
#     }

#     # 2. 调用 DIFY API 获取机器人的回复
#     bot_response = call_dify_api(payload)

#     # 检查 bot_response 是否有效
#     if not bot_response or "conversation_id" not in bot_response or "answer" not in bot_response:
#         raise HTTPException(status_code=500, detail="Failed to get a valid response from the bot")

#     # 确保 answer 是一个有效的字符串
#     answer = bot_response.get("answer", "Sorry, I don't have an answer for that.")

#     # 3. 存储机器人的消息
#     bot_message = store_bot_message(db, {"conversation_id": conversation_id, "answer": answer}, message.user_id)

#     # 返回响应
#     return {
#         "success": True,
#         "response": answer,
#         "chat_id": user_message.chat_id,
#         "conversation_id": conversation_id
#     }
# 2. 发送一条聊天消息
@app.post("/api/chat/message", response_model=dict)
def create_chat_message(message: CreateChatMessage, db: Session = Depends(get_db)):
    # 1. 存储用户的消息
    user_message = store_user_message(db, message.dict())

    payload = {
        "inputs": {},
        "query": message.message,
        "response_mode": "blocking",
        "conversation_id": "",  # Use empty string instead of potentially null value
        "user": str(message.user_id),  # Ensure user_id is a string
        "files": []
    }

    try:
        # 2. 调用 DIFY API 获取机器人的回复
        bot_response = call_dify_api(payload)
        print("Dify API Response:", bot_response)  # 添加日志

        # 确保 answer 是一个有效的字符串
        if bot_response and "answer" in bot_response:
            answer = bot_response.get("answer")
            conversation_id = bot_response.get("conversation_id", "") or message.conversation_id or f"conv_{message.user_id}_{user_message.chat_id}"
        else:
            answer = "I'm sorry, I couldn't process your request at the moment. Please try again later."
            conversation_id = message.conversation_id or f"conv_{message.user_id}_{user_message.chat_id}"
    
    except Exception as e:
        print(f"Error calling Dify API: {str(e)}")
        answer = "I apologize, but there was an error processing your request. Please try again later."
        conversation_id = message.conversation_id or f"conv_{message.user_id}_{user_message.chat_id}"

    # 3. 存储机器人的消息
    bot_message = store_bot_message(db, {"conversation_id": conversation_id, "answer": answer}, message.user_id)

    # 返回响应
    return {
        "success": True,
        "response": answer,  # This will always be a string now
        "chat_id": user_message.chat_id,
        "conversation_id": conversation_id  # This will always have a value
    }


# 3. 获取医生列表
@app.get("/api/doctors", response_model=DoctorDataResponse)
def get_doctors_endpoint(db: Session = Depends(get_db)):
    # 返回响应
    return {
        "success": True,
        "data": get_doctors(db)
    }


# 4. 获取用户预约记录
@app.get("/api/appointments/user/{user_id}", response_model=AppointmentDataResponse)
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
        raise HTTPException(status_code=400, detail="Unable to create appointment")

    doctor = db.query(Doctor).filter(Doctor.doctor_id == appointment.doctor_id).first()
    return {
        "success": True,
        "data": {
            "appointment_id": new_appointment.appointment_id,
            "doctor_name": doctor.name,
            "appointment_date": new_appointment.appointment_date,
            "status": new_appointment.status
        },
        "message": "Appointment successful!"
    }


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1")

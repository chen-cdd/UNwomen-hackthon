from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

<<<<<<< HEAD
=======

>>>>>>> d6a989f16b6942fc5b2ba734713a21b751d81a19
# 登录请求体
class LoginRequest(BaseModel):
    email: str
    password: str

# 用户注册请求体
class RegisterRequest(BaseModel):
    email: str
    fullname: str  # 添加 fullname 字段
    password: str

<<<<<<< HEAD
    
=======
>>>>>>> d6a989f16b6942fc5b2ba734713a21b751d81a19
class ChatHistoryResponse(BaseModel):
    chat_id: int
    user_id: int
    conversation_id: str
    message: str
    is_user: bool
    created_at: datetime

    class Config:
        orm_mode = True

class ChatHistoryDataResponse(BaseModel):
    success: bool
    data: List[ChatHistoryResponse]

class CreateChatMessage(BaseModel):
    user_id: int
    conversation_id: str
    message: str
    is_user: bool

    class Config:
        orm_mode = True  # 允许从 ORM 对象转换

class DoctorResponse(BaseModel):
    doctor_id: int
    name: str
    specialty: str
    availability: dict  # 格式：{"Monday": "9:00-17:00", "Wednesday": "9:00-17:00"}
    contact_info: dict  # 格式：{"phone": "123-4567", "email": "doctor@hospital.com"}

    class Config:
        orm_mode = True

class DoctorDataResponse(BaseModel):
    success: bool
    data: List[DoctorResponse]

class AppointmentResponse(BaseModel):
    appointment_id: int
    doctor_name: str
    appointment_date: datetime
    status: str
    notes: str

    class Config:
        orm_mode = True

class AppointmentDataResponse(BaseModel):
    success: bool
    data: List[AppointmentResponse]

class AppointmentCreate(BaseModel):
    user_id: int
    doctor_id: int
    appointment_date: datetime
    status: str = "scheduled"
    notes: Optional[str] = None

    class Config:
        orm_mode = True

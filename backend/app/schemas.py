from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

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

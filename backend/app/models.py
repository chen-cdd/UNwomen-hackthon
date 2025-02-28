from sqlalchemy import Column, Integer, String, Text, Date, DateTime, ForeignKey, Enum, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.types import TIMESTAMP
from .database import Base
import enum
from sqlalchemy import func


# 枚举类型
class AppointmentStatus(str, enum.Enum):
    scheduled = "scheduled"
    completed = "completed"
    cancelled = "cancelled"


# 聊天记录表
class ChatHistory(Base):
    __tablename__ = 'chat_history'
    chat_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    conversation_id = Column(String, index=True)
    message = Column(Text)
    is_user = Column(Integer)  # 1: 用户，0: 系统
    created_at = Column(TIMESTAMP, server_default=func.now())

# 用户模型
class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True)
    password_hash = Column(String(255))
    created_at = Column(TIMESTAMP, nullable=False, default=func.now())  # 自动填充当前时间


# 预约模型
class Appointment(Base):
    __tablename__ = "appointments"

    appointment_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)
    doctor_id = Column(Integer, ForeignKey("doctors.doctor_id"), nullable=True)
    appointment_date = Column(TIMESTAMP, nullable=False)
    status = Column(Enum(AppointmentStatus), nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, default=func.now())  # 自动填充当前时间

# 医生模型
class Doctor(Base):
    __tablename__ = "doctors"

    doctor_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    specialty = Column(String(50), nullable=False)
    availability = Column(JSON, nullable=True)
    contact_info = Column(JSON, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, default=func.now())  # 自动填充当前时间


# 用户档案模型
class UserProfile(Base):
    __tablename__ = "user_profiles"

    profile_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    birth_date = Column(Date, nullable=True)
    menstrual_status = Column(String(50), nullable=True)
    health_conditions = Column(JSON, nullable=True)
    privacy_settings = Column(JSON, nullable=True)
    last_updated = Column(TIMESTAMP, nullable=False)

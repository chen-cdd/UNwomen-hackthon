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

    fullname = Column(String)  # 添加 fullname 字段
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
    doctor_name = Column(String(255), nullable=True)
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

# 事件模型
class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True, comment="事件ID")
    user_id = Column(Integer, index=True, nullable=False, comment="用户ID")
    title = Column(String, nullable=False, comment="事件标题")
    start_date = Column(DateTime, nullable=False, comment="事件开始时间")
    end_date = Column(DateTime, nullable=False, comment="事件结束时间")

# 月经记录模型
class CycleRecord(Base):
    __tablename__ = "cycle_records"

    record_id = Column(Integer, primary_key=True, autoincrement=True, comment="记录ID")
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False, index=True, comment="用户ID")
    cycle_start_date = Column(Date, nullable=False, comment="周期开始日期")
    cycle_end_date = Column(Date, nullable=True, comment="周期结束日期")
    symptoms = Column(JSON, nullable=True, default=[], comment="症状")  # 默认空列表
    mood = Column(String(50), nullable=True, default="", comment="情绪")  # 默认空字符串
    notes = Column(Text, nullable=True, default="", comment="备注")  # 默认空字符串
    created_at = Column(TIMESTAMP, nullable=False, default=func.now())  # 自动填充当前时间

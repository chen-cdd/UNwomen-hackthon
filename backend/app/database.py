from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

# 创建数据库连接引擎
engine = create_engine(DATABASE_URL, connect_args={"charset": "utf8mb4"})

# 创建 Session 类
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 基础类，所有的模型都应继承这个类
Base = declarative_base()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import OPENAI_API_KEY  # config.py에서 환경 변수 가져옴
import os

DATABASE_URL = "mysql+pymysql://fastapi_user:password123@localhost:3306/gpt_translator"

# 데이터베이스 연결
engine = create_engine(DATABASE_URL, echo=True)

# 세션 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ORM 모델의 Base 클래스
Base = declarative_base()

# 데이터베이스 세션을 가져오는 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

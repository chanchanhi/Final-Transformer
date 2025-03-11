import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError
from config import OPENAI_API_KEY  # config.py에서 환경 변수 가져옴
import os

DATABASE_URL = os.getenv("DATABASE_URL")

# 데이터베이스 연결 재시도 로직 추가 (최대 10회)
attempt = 0
while attempt < 10:
    try:
        engine = create_engine(DATABASE_URL)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        print("✅ Successfully connected to the database!")
        break
    except OperationalError:
        attempt += 1
        print(f"🚨 Database connection failed. Retrying in 5 seconds... ({attempt}/10)")
        time.sleep(5)

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

import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError
from app.config import DATABASE_URL  # config.py에서 환경 변수 가져옴
import os

DATABASE_URL = os.getenv("DATABASE_URL")

# ✅ Base를 먼저 정의
Base = declarative_base()

# 데이터베이스 연결 재시도 로직 추가
MAX_RETRIES = 5
for i in range(MAX_RETRIES):
    try:
        engine = create_engine(DATABASE_URL)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        print("✅ 데이터베이스 연결 성공")
        break
    except OperationalError:
        print(f"⚠️ DB 연결 실패, {i+1}번째 재시도 중...")
        time.sleep(2)
else:
    raise Exception("🚨 최대 재시도 횟수 초과: DB 연결 실패")
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

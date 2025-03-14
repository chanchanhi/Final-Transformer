from app.db.database import engine, Base
from app.db import models
from fastapi import FastAPI
from app.routes import users, translate
from fastapi.middleware.cors import CORSMiddleware

# 테이블 생성
Base.metadata.create_all(bind=engine)

app = FastAPI()

# API 라우터 등록
app.include_router(users.router)
app.include_router(translate.router)

origins = [
    "chrome-extension://dkidpaekmpndoegjcppbclfaidjhljob",  # 크롬 확장 프로그램의 ID로 변경
    "http://localhost:8000",  # 개발 중인 로컬 서버 주소
    # 필요에 따라 추가적인 출처를 여기에 추가
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 모든 출처 허용 (배포 시에는 특정 도메인으로 제한해야 함)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}

from db.database import engine, Base
from fastapi import FastAPI
from routes import users, translate
from fastapi.middleware.cors import CORSMiddleware

# 테이블 생성
Base.metadata.create_all(bind=engine)

app = FastAPI()

# API 라우터 등록
app.include_router(users.router)
app.include_router(translate.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 출처 허용 (배포 시에는 특정 도메인으로 제한해야 함)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}

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

# CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인 허용 (보안이 필요하면 특정 도메인만 허용)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "FastAPI 서버 정상 작동 중"}

@app.post("/translate")
async def translate(text: str):
    return {"translated_text": f"번역된 결과: {text}"}



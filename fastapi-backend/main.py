from db.database import engine, Base
from fastapi import FastAPI
from routes import users, translate

# 테이블 생성
Base.metadata.create_all(bind=engine)

app = FastAPI()

# API 라우터 등록
app.include_router(users.router)
app.include_router(translate.router)

@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}

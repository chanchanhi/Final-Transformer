from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from models.models import User
from pydantic import BaseModel

router = APIRouter()

# User 생성 요청 모델
class UserCreate(BaseModel):
    google_id: str
    email: str
    username: str

# 사용자 추가 API
@router.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        google_id=user.google_id,
        email=user.email,
        username=user.username
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

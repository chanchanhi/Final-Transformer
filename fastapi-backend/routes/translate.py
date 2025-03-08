from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config import OPENAI_API_KEY
from openai import OpenAI
from db.database import get_db
from models.models import Translation
from pydantic import BaseModel
from datetime import datetime
import os

router = APIRouter()

# OpenAI API 키 설정
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

# 요청 데이터 모델
class TranslateRequest(BaseModel):
    user_id: int
    text: str

# 번역 API 엔드포인트
@router.post("/translate")
def translate_text(request: TranslateRequest, db: Session = Depends(get_db)):
    # GPT API 호출
    response = client.Completion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": request.text}]
    )

    translated_text = response["choices"][0]["message"]["content"]

    # 번역 결과 저장
    new_translation = Translation(
        user_id=request.user_id,
        original_text=request.text,
        translated_text=translated_text,
        created_at=datetime.utcnow()
    )

    db.add(new_translation)
    db.commit()
    db.refresh(new_translation)

    return {"translated_text": translated_text}

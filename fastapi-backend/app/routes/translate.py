from fastapi import APIRouter, Depends
from app.services.gpt_service import translate_text
from app.db.database import get_db
from app.db.models import Translation
from sqlalchemy.orm import Session
#from app.config import OPENAI_API_KEY
#from openai import OpenAI
from pydantic import BaseModel
from datetime import datetime
import os

router = APIRouter(prefix="/api/translate", tags=["translate"])

# 요청 데이터 모델
class TranslateRequest(BaseModel):
    user_id: int
    text: str

# 번역 API 엔드포인트
@router.post("/")
def translate_request(request: TranslateRequest, db: Session = Depends(get_db)):
    """
    신조어 및 어려운 단어를 탐지하고 표준어 및 쉬운 표현으로 변환하는 API
    """
    try:
        translated_text = translate_text(request.text)  # GPT 서비스 호출

        # 🔹 번역 결과를 DB에 저장
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

    except Exception as e:
        return {"error": f"번역 중 오류 발생: {str(e)}"}
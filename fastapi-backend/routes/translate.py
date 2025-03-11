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
    """
    사용자가 입력한 문장에서 신조어나 어려운 단어를 감지하여 
    표준어 및 쉬운 표현으로 변환 후 반환하는 API 엔드포인트
    """

    # 🔹 GPT 프롬프트 (사용자의 요구사항에 맞춤)
    prompt = f"""
    너는 한국어 신조어 및 어려운 한자어, 전문 용어를 감지하고 표준어 및 쉬운 표현으로 변환하는 번역가야.
    사용자가 선택한 문장에 포함된 신조어 및 어려운 단어를 굵은 글씨로 강조 표시한 후, 그 아래에 해당 단어의 쉬운 표현을 제공해.

    입력 문장: "{request.text}"

    작업 방식:
    1. 입력된 문장에서 신조어, 어려운 한자어, 전문 용어를 탐지하여 굵은 글씨(`**이렇게**`)로 강조.
    2. 각 강조된 단어에 대한 쉬운 표현을 제공.
    3. 최종적으로 변환된 문장을 출력.

    출력 예시:
    - 원문: "이거 완전 **디토합니다**. 이런 **그 잡채** 스타일 너무 좋아!"
    - 변환: "이거 완전 **동의합니다**. 이런 **정확한** 스타일 너무 좋아!"

    주의사항:
    - 반드시 번역된 문장만 반환해야 함.
    - 출력 형식 외에는 어떠한 설명도 포함하지 말 것.
    """

    # 🔹 GPT API 호출
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # 최신 GPT 모델 사용
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        translated_text = response.choices[0].message.content.strip()

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
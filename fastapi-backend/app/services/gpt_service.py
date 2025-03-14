import openai
from app.config import OPENAI_API_KEY

# OpenAI API 클라이언트 생성
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def translate_text(text: str) -> str:
    """
    GPT-4를 사용하여 신조어 및 어려운 단어를 번역하는 함수
    """
    prompt = f"""
    너는 한국어 신조어 및 어려운 한자어, 전문 용어를 감지하고 표준어 및 쉬운 표현으로 변환하는 번역가야.
    입력 문장: "{text}"

    1. 신조어 및 어려운 단어를 감지하여 굵은 글씨(**이렇게**)로 강조.
    2. 각 강조된 단어에 대한 쉬운 표현을 제공.
    3. 최종적으로 변환된 문장을 출력.

    출력 예시:
    - 원문: "이거 완전 **디토합니다**. 이런 **그 잡채** 스타일 너무 좋아!"
    - 변환: "이거 완전 **동의합니다**. 이런 **정확한** 스타일 너무 좋아!"
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )
        return response.choices[0].message.content.strip()
    except openai.error.OpenAIError as e:
        return f"GPT 오류 발생: {str(e)}"


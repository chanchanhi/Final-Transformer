from dotenv import load_dotenv
import os

# .env 파일 로드 (fastapi-backend 디렉토리에 위치해야 함)
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")

if not OPENAI_API_KEY:
    raise ValueError("🚨 OPENAI_API_KEY가 설정되지 않았습니다. .env 파일을 확인하세요!")

if not DATABASE_URL:
    raise ValueError("🚨 DATABASE_URL가 설정되지 않았습니다. .env 파일을 확인하세요!")
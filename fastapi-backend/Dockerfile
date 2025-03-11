# 1️⃣ Python 3.12 이미지 사용
FROM python:3.12

# 2️⃣ 작업 디렉토리 설정
WORKDIR /app

# 3️⃣ 필요 파일 복사 및 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 4️⃣ 전체 프로젝트 복사
COPY . .

# 5️⃣ uvicorn 실행을 위한 명령어 명확하게 지정
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


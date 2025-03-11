# Node.js 최신 버전 사용
FROM node:18

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 파일 복사
COPY package.json package-lock.json ./
RUN npm install

# 소스 코드 복사
COPY . .

# 서버 실행
CMD ["node", "server.js"]

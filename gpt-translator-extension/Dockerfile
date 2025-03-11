# Node.js 최신 버전 사용
FROM node:18

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 파일 복사 및 의존성 설치
COPY package.json package-lock.json ./
RUN npm install

# 소스 코드 복사
COPY . .

# React 빌드 실행 (크롬 확장 프로그램은 정적 파일로 빌드됨)
RUN npm run build

# 컨테이너 시작 시 React 앱 실행 (크롬 확장 프로그램은 정적 파일이므로 필요 없음)
CMD ["echo", "React build complete. Manually load the extension from dist folder."]

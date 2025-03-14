FROM nginx:latest

# 작업 디렉토리를 nginx 설정 디렉터리로 설정
WORKDIR /etc/nginx

# SSL 인증서 복사 (절대 경로로 변경)
#COPY ../certs/cert.pem /etc/nginx/certs/cert.pem
#COPY ../certs/key.pem /etc/nginx/certs/key.pem

# Nginx 설정 파일 복사
COPY nginx.conf /etc/nginx/nginx.conf

# 기본 설정 파일 제거 (필요한 경우)
RUN rm /etc/nginx/conf.d/default.conf


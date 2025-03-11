const express = require("express");
const { createProxyMiddleware } = require("http-proxy-middleware");
const cors = require("cors");
require("dotenv").config();

const app = express();
const PORT = 3001;

// CORS 설정
app.use(cors());

// FastAPI 서버 프록시 설정 (HTTPS 요청을 FastAPI로 전달)
app.use(
  "/api",
  createProxyMiddleware({
    target: "http://fastapi:8000", // Docker 네트워크 내부에서 FastAPI 서비스명 사용
    changeOrigin: true,
    pathRewrite: { "^/api": "" }, // "/api" 경로를 제거하여 FastAPI에서 올바르게 인식
  })
);

app.listen(PORT, () => {
  console.log(`Proxy server running at http://localhost:${PORT}`);
});

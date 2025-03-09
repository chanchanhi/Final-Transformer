import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { resolve } from "path";
import { copyFileSync, existsSync, mkdirSync } from "fs";



// https://vite.dev/config/
export default defineConfig({
  plugins: [
    react(),
    {
      name: "copy-content-scripts",
      closeBundle() {
        // dist 폴더가 존재하지 않으면 생성
        if (!existsSync("dist")) {
          mkdirSync("dist", { recursive: true });
        }
        // content.js와 background.js를 dist 폴더로 복사
        copyFileSync("src/content/content.js", "dist/content.js");
        copyFileSync("src/content/background.js", "dist/background.js");
        console.log("✅ content.js & background.js copied to dist/");
      },
    },
  ],
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, "index.html"),
      },
    },
  },
});
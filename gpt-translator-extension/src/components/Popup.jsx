/*
import { useState } from "react";
import { translateText } from "../api/translate";

const Popup = () => {
  const [text, setText] = useState("");
  const [translatedText, setTranslatedText] = useState("");

  const handleTranslate = async () => {
    if (!text) return;
    const result = await translateText(text);
    setTranslatedText(result);
  };

  return (
    <div style={{ width: "300px", padding: "20px" }}>
      <h2>GPT 번역기</h2>
      <textarea
        placeholder="번역할 문장을 입력하세요"
        value={text}
        onChange={(e) => setText(e.target.value)}
        rows="3"
        style={{ width: "100%", padding: "5px" }}
      />
      <button onClick={handleTranslate} style={{ marginTop: "10px", padding: "5px 10px" }}>
        번역하기
      </button>
      {translatedText && (
        <div>
          <h3>번역 결과</h3>
          <p>{translatedText}</p>
        </div>
      )}
    </div>
  );
};

export default Popup;
**/

// Popup.jsx
import { useState, useEffect } from "react";

const API_URL = "/api/translate";  // Nginx 프록시를 통한 FastAPI 요청

function Popup() {
    const [text, setText] = useState("");
    const [translatedText, setTranslatedText] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");
    const [history, setHistory] = useState([]);

    useEffect(() => {
        // 선택한 텍스트 가져오기
        chrome.storage.local.get(["selectedText"], (result) => {
            if (result.selectedText) {
                setText(result.selectedText);
                handleTranslate(result.selectedText);
            }
        });

        // 번역 기록 불러오기
        chrome.storage.local.get(["translationHistory"], (result) => {
            if (result.translationHistory) {
                setHistory(result.translationHistory);
            }
        });
    }, []);

    const handleTranslate = async (text) => {
        setLoading(true);
        setError("");

        try {
            const response = await fetch(API_URL, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ text }),
            });

            if (!response.ok) {
                throw new Error(`번역 실패 (에러 코드: ${response.status})`);
            }

            const data = await response.json();
            setTranslatedText(data.translated_text);

            // 번역 기록 저장
            const newHistory = [{ text, translatedText: data.translated_text }, ...history];
            setHistory(newHistory);
            chrome.storage.local.set({ translationHistory: newHistory });
        } catch (error) {
            setError(error.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="popup-container">
            <h2>GPT 번역기</h2>
            <p><strong>원문:</strong> {text}</p>
            {loading ? <p>번역 중...</p> : <p><strong>번역:</strong> {translatedText}</p>}
            {error && <p className="error">{error}</p>}

            <h3>번역 기록</h3>
            <ul>
                {history.map((entry, index) => (
                    <li key={index}>
                        <p><strong>원문:</strong> {entry.text}</p>
                        <p><strong>번역:</strong> {entry.translatedText}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default Popup;

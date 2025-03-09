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

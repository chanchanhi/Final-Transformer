/**
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    console.log("Received message:", request);
    
    if (request.action === "translateSelection") {
        let selectedText = window.getSelection().toString().trim();
        if (!selectedText) {
            alert("번역할 텍스트를 선택하세요.");
            return;
        }

        fetch("https://127.0.0.1:8000/translate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ user_id: 1, text: selectedText })
        })
        .then(response => response.json())
        .then(data => {
            alert(`번역 결과: ${data.translated_text}`);
        })
        .catch(error => {
            console.error("Translation failed:", error);
        });

        sendResponse({ success: true });
    }
});
*/
// 사용자가 문장을 드래그했을 때 감지
document.addEventListener("mouseup", () => {
    const selectedText = window.getSelection().toString().trim();
    
    if (selectedText) {
        chrome.runtime.sendMessage({ action: "TEXT_SELECTED", text: selectedText });
    }
});


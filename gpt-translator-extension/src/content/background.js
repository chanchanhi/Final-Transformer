chrome.runtime.onInstalled.addListener(() => {
    chrome.contextMenus.create({
        id: "translateText",
        title: "GPT 번역하기",
        contexts: ["selection"]
    });
});
/*
chrome.contextMenus.onClicked.addListener((info, tab) => {
    if (info.menuItemId === "translateText") {
        chrome.tabs.sendMessage(tab.id, { action: "getSelectedText" }, (response) => {
            if (chrome.runtime.lastError) {
                console.error("Error sending message:", chrome.runtime.lastError.message);
                return;
            }
            
            const selectedText = response?.text;
            if (!selectedText) {
                console.error("No text selected.");
                return;
            }

            console.log("선택된 텍스트:", selectedText);

            fetch("/api/translate", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ user_id: 1, text: selectedText })
            })
            .then(response => response.json())
            .then(data => {
                console.log("번역 결과:", data.translated_text);
                chrome.notifications.create({
                    type: "basic",
                    iconUrl: "icon.png",
                    title: "GPT 번역 결과",
                    message: data.translated_text
                });
            })
            .catch(error => {
                console.error("Translation failed:", error);
            });
        });
    }
});
**/
chrome.contextMenus.onClicked.addListener((info) => {
    if (info.menuItemId === "gptTranslate") {
        // 선택한 텍스트를 Popup으로 전달
        chrome.storage.local.set({ selectedText: info.selectionText });

        // 팝업 창 강제 열기
        chrome.windows.create({
            url: chrome.runtime.getURL("popup.html"),
            type: "popup",
            width: 400,
            height: 500
        });
    }
});
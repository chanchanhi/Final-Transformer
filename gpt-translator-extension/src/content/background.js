chrome.runtime.onInstalled.addListener(() => {
    chrome.contextMenus.create({
        id: "translateText",
        title: "GPT 번역하기",
        contexts: ["selection"]
    });
});

chrome.contextMenus.onClicked.addListener((info, tab) => {
    if (info.menuItemId === "translateText") {
        // content.js가 로드되었는지 확인 후 메시지 전송
        chrome.scripting.executeScript({
            target: { tabId: tab.id },
            files: ["content.js"]
        }, () => {
            chrome.tabs.sendMessage(tab.id, { action: "translateSelection" }, (response) => {
                if (chrome.runtime.lastError) {
                    console.error("Error sending message:", chrome.runtime.lastError.message);
                } else {
                    console.log("Message sent successfully:", response);
                }
            });
        });
    }
});



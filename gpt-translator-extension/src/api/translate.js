export const translateText = async (text) => {
    const response = await fetch("/api/translate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_id: 1, text })
    });

    const data = await response.json();
    return data.translated_text;
};

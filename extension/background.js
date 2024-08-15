document.addEventListener("DOMContentLoaded", () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        chrome.tabs.sendMessage(tabs[0].id, { action: "getEmailContent" }, (response) => {
            if (response) {
                document.getElementById("content").textContent = response.content;
            } else {
                document.getElementById("content").textContent = "Failed to retrieve email content.";
            }
        });
    });
});
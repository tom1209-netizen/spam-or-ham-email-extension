function getEmailContent() {
    // Look for the email body in Gmail
    const emailBody = document.querySelector(".ii.gt");
    if (emailBody) {
        return emailBody.innerText;
    }
    return "No email content found.";
}

// Listen for messages from the popup
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "getEmailContent") {
        const content = getEmailContent();
        sendResponse({ content });
    }
});
document.addEventListener("DOMContentLoaded", () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        chrome.tabs.sendMessage(tabs[0].id, { action: "getEmailContent" }, (response) => {
            if (response) {
                const emailContent = response.content;
                document.getElementById("content").textContent = emailContent;

                const url = 'https://spam-or-ham-email-extension.onrender.com/predict';

                fetch(url, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ text: emailContent }),  // Send the email content as part of the POST request
                })
                .then(response => response.json())
                .then(data => {
                    console.log(data)
                    document.getElementById("result").textContent = data.prediction;
                })

            } else {
                document.getElementById("content").textContent = "Failed to retrieve email content.";
            }
        });
    });
});
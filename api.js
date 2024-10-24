const BOT_TOKEN = "8000283320:AAHhULAbMgrx93DRRumbiItAHRR5XFnoFuE"; // Replace with your Telegram bot token

        document.getElementById("contactForm").addEventListener("submit", async (e) => {
            e.preventDefault();

            const name = document.getElementById("name").value;
            const email = document.getElementById("email").value;
            const phone = document.getElementById("phone").value;
            const username = document.getElementById("username").value;
            const messageContent = document.getElementById("message").value;

            if (!username.startsWith("@")) {
                alert("Please enter a valid Telegram username starting with '@'.");
                return;
            }

            const message = `
📇 *New Contact Message*\n
👤 Name: ${name}\n
📧 Email: ${email}\n
📱 Phone: ${phone}\n
💬 Message: ${messageContent}\n
Contacting: ${username}`;

            try {
                const response = await fetch(`https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        chat_id: CHAT_ID,
                        text: message,
                        parse_mode: "Markdown"
                    })
                });

                if (response.ok) {
                    const result = await response.json();
                    document.getElementById("resultMessage").innerHTML = "Message sent successfully!";
                    document.getElementById("contactForm").reset();
                } else {
                    const error = await response.json();
                    document.getElementById("resultMessage").innerHTML = `Failed to send message: ${error.description}`;
                }
            } catch (error) {
                document.getElementById("resultMessage").innerHTML = "Error: " + error.message;
            }
        });

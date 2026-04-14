import os
import requests

def send(message):

    token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")

    if not token or not chat_id:
        print("❌ Missing Telegram config")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    try:
        requests.post(url, data={
            "chat_id": chat_id,
            "text": message
        })
        print("✅ Sent")
    except Exception as e:
        print("❌ Error:", e)

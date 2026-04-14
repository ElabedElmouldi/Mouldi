

import os
import requests

def send(message):

    token = os.getenv("8439548325:AAHOBBHy7EwcX3J5neIaf6iJuSjyGJCuZ68")
    chat_id = os.getenv("5067771509")

    if not token or not chat_id:
        print("❌ Missing BOT_TOKEN or CHAT_ID")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    try:
        requests.post(url, data={
            "chat_id": chat_id,
            "text": message
        })
        print("✅ Message sent")
    except Exception as e:
        print("❌ Telegram error:", e)



im

import os
import requests

def send_message(text):

    token = os.getenv("8439548325:AAHOBBHy7EwcX3J5neIaf6iJuSjyGJCuZ68")   # ✅ variable name
    chat_id = os.getenv("5067771509")   # ✅ variable name

    if not token or not chat_id:
        print("Missing BOT_TOKEN or CHAT_ID")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    requests.post(url, data={
        "chat_id": chat_id,
        "text": text
    })

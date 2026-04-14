

import os
import requests

def send(msg):

    token = os.getenv("8439548325:AAHOBBHy7EwcX3J5neIaf6iJuSjyGJCuZ68")
    chat = os.getenv("5067771509")

    if not token or not chat:
        return

    requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        data={"chat_id": chat, "text": msg}
    )



)



import os
import requests

def send(msg):

    token = os.getenv("8738851163:AAEe7YI7p05xSxsRSruu34taIaUk47aHCQY")
    chat = os.getenv("5067771509")

    if not token or not chat:
        return

    requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        data={"chat_id": chat, "text": msg}
    )



)

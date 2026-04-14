import requests

TOKEN = "PUT_YOUR_BOT_TOKEN_HERE"
CHAT_ID = "5067771509"

def send(msg):

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": msg
    }

    requests.post(url, data=data)

import requests

BOT_TOKEN = "8439548325:AAHOBBHy7EwcX3J5neIaf6iJuSjyGJCuZ68"
CHAT_ID = "5067771509"

def send(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": text
    })


def send_dashboard(balance, trades_count):

    text = f"""
📊 DASHBOARD

💰 Balance: {balance}
📦 Open Trades: {trades_count}
"""

    send(text)

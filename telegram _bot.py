import requests
from config import BOT_TOKEN, CHAT_ID
from portfolio import portfolio

def send(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})


def handle_command(text):

    text = text.lower()

    if text == "/balance":
        send(f"💰 Balance: {portfolio['balance']}")

    if text == "/positions":
        send(str(portfolio["open_trades"]))

    if text == "/start":
        send("🤖 Bot Started")

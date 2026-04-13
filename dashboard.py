from portfolio import portfolio
from telegram_bot import send

def show_dashboard():

    text = f"""
📊 DASHBOARD

💰 Balance: {portfolio['balance']}
📦 Trades: {len(portfolio['open_trades'])}
"""

    send(text)

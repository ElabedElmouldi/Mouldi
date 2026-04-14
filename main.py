from strategy import get_signal
from risk import check_risk
from execution import execute_trade
from portfolio import Portfolio
from telegram import send

portfolio = Portfolio()

def run():

    print("🚀 GOD MODE V2 PRO STARTED")

    while True:

        data = {
            "momentum": 1.2,
            "volatility": 0.7
        }

        signal = get_signal(data)

        if not check_risk(data):
            continue

        result = execute_trade(signal)

        portfolio.update(result)

        send(f"Signal: {signal} | Balance: {portfolio.balance}")

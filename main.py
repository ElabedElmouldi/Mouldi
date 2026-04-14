import time

from engine import Engine
from strategy.explosion import ExplosionStrategy
from scanner import scan
from trader import open_trade, update_trades
from portfolio import portfolio
from telegram_bot import send, send_dashboard
from data import get_data


def get_price(symbol):
    return get_data(symbol)['c'].iloc[-1]


def run():

    strategy = ExplosionStrategy()
    engine = Engine(strategy)

    send("🤖 BOT STARTED (PAPER MODE)")

    while True:

        signals = scan(engine)

        for s in signals[:3]:
            open_trade(s["symbol"], s["price"], s["score"])
            send(f"🚀 SIGNAL {s['symbol']}")

        update_trades(get_price, send)

        send_dashboard(
            portfolio["balance"],
            len(portfolio["open_trades"])
        )

        time.sleep(30)


run()

import time

from engine import Engine
from strategy.explosion import ExplosionStrategy
from scanner import scan
from trader import open_trade, update_trades
from telegram_bot import send
from data import get_data
from portfolio import portfolio
from dashboard import show_dashboard

def get_price(symbol):
    return get_data(symbol)['c'].iloc[-1]


def run():

    strategy = ExplosionStrategy()
    engine = Engine(strategy)

    send("🤖 BOT STARTED")

    while True:

        signals = scan(engine)

        for s in signals[:3]:
            open_trade(s["symbol"], s["price"], s["score"])

        update_trades(get_price, send)

        show_dashboard()

        time.sleep(30)


run()

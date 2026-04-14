from scanner import scan_market
from watcher import add_coin, check_explosion, watchlist
from telegram import send
from strategy_entry import confirm_entry
from trade_manager import open_trade, check_trade, trades

import time
import random

print("🚀 EXPLOSION AI SIMULATION STARTED")

price_memory = {}

def simulate_price(symbol, base_price):

    if symbol not in price_memory:
        price_memory[symbol] = base_price

    move = random.uniform(-1, 2)

    price_memory[symbol] *= (1 + move / 100)

    return round(price_memory[symbol], 2)


def fake_market():

    coins = []

    for i in range(200):
        coins.append({
            "symbol": f"COIN{i}",
            "price": 100,
            "momentum": random.uniform(1, 2),
            "volume": random.uniform(1, 2),
            "trend_5m": random.choice(["UP", "DOWN"]),
            "trend_1h": random.choice(["UP", "DOWN"]),
            "volatility": random.uniform(0.8, 2),
            "near_resistance": random.choice([True, False])
        })

    return coins


while True:

    market = fake_market()

    top_coins = scan_market(market)

    # 📊 إرسال أفضل العملات
    msg = "📊 TOP EXPLOSION CANDIDATES\n\n"

    for c in top_coins:
        msg += f"🔹 {c['symbol']} | Score: {c['score']}\n"
        add_coin(c)

    send(msg)

    # 🔥 مراقبة + دخول
    for symbol in list(watchlist.keys()):

        new_price = simulate_price(symbol, 100)

        triggered, change = check_explosion(symbol, new_price)

        if triggered:

            coin_data = {
                "volume": random.uniform(1.4, 2),
                "trend_5m": "UP",
                "volatility": random.uniform(0.8, 2)
            }

            if confirm_entry(coin_data, change):

                open_trade(symbol, new_price)

                send(f"""
🟢 ENTRY SIGNAL

💰 Symbol: {symbol}
📥 Entry: {new_price}
🎯 Target: +5%
🛑 Stop: -2%
""")

        # 📊 متابعة الصفقة
        result = check_trade(symbol, new_price)

        if result == "TP":
            send(f"🎯 TAKE PROFIT 🚀 {symbol}")
            del trades[symbol]

        elif result == "SL":
            send(f"⚠️ STOP LOSS ❌ {symbol}")
            del trades[symbol]

    time.sleep(10)

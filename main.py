from scanner import scan_market
from watcher import add_to_watchlist, update_watchlist
from telegram import send
import random
import time

print("🚀 REAL-TIME SCANNER v2 STARTED")

# fake live market
def generate_market():

    coins = []

    for i in range(600):

        coins.append({
            "symbol": f"COIN{i}",
            "price": 100 + random.randint(-5, 5),
            "momentum": random.uniform(1, 2),
            "volume": random.uniform(1, 2),
            "trend_5m": random.choice(["UP", "DOWN"]),
            "trend_1h": random.choice(["UP", "DOWN"]),
            "volatility": random.uniform(0.8, 2),
            "near_resistance": random.choice([True, False])
        })

    return coins


while True:

    market = generate_market()

    results = scan_market(market)

    print("\n💥 TOP EXPLOSION CANDIDATES:")

    for c in results[:5]:

        print(c["symbol"], c["score"])

        add_to_watchlist(c)

        send(f"""
💥 EXPLOSION ALERT
Symbol: {c['symbol']}
Score: {c['score']}
Price: {c['price']}
""")

    # simulate tracking
    for c in results[:3]:

        change = update_watchlist(c["symbol"], c["price"] + random.randint(-3, 6))

        if change and change > 3:
            send(f"📈 {c['symbol']} UP {change:.2f}%")

    time.sleep(10)


from portfolio import portfolio
from config import RISK_PER_TRADE

def open_trade(symbol, price, score):

    if symbol in portfolio["open_trades"]:
        return

    size = portfolio["balance"] * RISK_PER_TRADE

    portfolio["open_trades"][symbol] = {
        "entry": price,
        "tp": price * 1.02,
        "sl": price * 0.99,
        "size": size,
        "score": score
    }


def update_trades(get_price, send):

    for s in list(portfolio["open_trades"].keys()):

        price = get_price(s)
        trade = portfolio["open_trades"][s]

        if price >= trade["tp"]:
            portfolio["balance"] += trade["size"] * 0.02
            send(f"🟢 TP {s}")
            del portfolio["open_trades"][s]

        elif price <= trade["sl"]:
            portfolio["balance"] -= trade["size"] * 0.01
            send(f"🔴 SL {s}")
            del portfolio["open_trades"][s]

trades = {}

def open_trade(symbol, price):

    trades[symbol] = {
        "entry": price,
        "tp": price * 1.05,
        "sl": price * 0.98
    }

def check_trade(symbol, price):

    if symbol not in trades:
        return None

    trade = trades[symbol]

    if price >= trade["tp"]:
        return "TP"

    if price <= trade["sl"]:
        return "SL"

    return None

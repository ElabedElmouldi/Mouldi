watchlist = {}

def add_coin(coin):

    symbol = coin["symbol"]

    if symbol not in watchlist:
        watchlist[symbol] = {
            "entry": coin["price"],
            "score": coin["score"],
            "triggered": False
        }


def check_explosion(symbol, current_price):

    if symbol not in watchlist:
        return False, 0

    data = watchlist[symbol]

    entry = data["entry"]

    change = (current_price - entry) / entry * 100

    if change >= 1.5 and not data["triggered"]:
        data["triggered"] = True
        return True, change

    return False, change

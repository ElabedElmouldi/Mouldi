
active_watchlist = {}

def add_to_watchlist(coin):

    active_watchlist[coin["symbol"]] = {
        "entry": coin["price"],
        "score": coin["score"]
    }


def update_watchlist(symbol, new_price):

    if symbol not in active_watchlist:
        return None

    entry = active_watchlist[symbol]["entry"]

    change = (new_price - entry) / entry * 100

    return change

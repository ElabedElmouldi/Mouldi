def trend_strategy(data):
    return data["trend"] * 2

def mean_reversion(data):
    return (50 - data["rsi"]) / 10

def breakout(data):
    return data["volume"] * data["momentum"]

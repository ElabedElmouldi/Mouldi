def get_signal(data):

    score = data["momentum"] - data["volatility"]

    if score > 0.5:
        return "BUY"
    elif score < -0.5:
        return "SELL"

    return "HOLD"

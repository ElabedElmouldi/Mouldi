def alpha_v2(data):

    score = data["momentum"]*1.5 - data["volatility"]*1.2 + data["volume_spike"]*0.5

    if score > 0.7:
        return "BUY"
    elif score < -0.7:
        return "SELL"
    return "HOLD"

def risk_check(data):

    if data["volatility"] > 2.5:
        return False

    if data["rsi"] > 80 or data["rsi"] < 20:
        return False

    return True

def risk_check(data, drawdown):

    if drawdown > 0.2:
        return False

    if data["volatility"] > 2:
        return False

    return True
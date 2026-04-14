def confirm_entry(data, change):

    if change < 1.5:
        return False

    if data["volume"] < 1.5:
        return False

    if data["trend_5m"] != "UP":
        return False

    if data["volatility"] > 1.8:
        return False

    return True

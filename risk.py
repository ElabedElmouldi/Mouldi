def check_risk(data):

    if data["volatility"] > 2:
        return False

    return True

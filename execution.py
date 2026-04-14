def execute_trade(signal):

    if signal == "BUY":
        return 1

    if signal == "SELL":
        return -1

    return 0

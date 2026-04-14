def execute(signal, size):

    if signal == "BUY":
        return 1
    if signal == "SELL":
        return -1
    return 0
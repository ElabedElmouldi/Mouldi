def backtest(data, strategy):

    balance = 1000

    for d in data:

        signal = strategy(d)

        if signal == "BUY":
            balance += 1
        elif signal == "SELL":
            balance -= 1

    return balance

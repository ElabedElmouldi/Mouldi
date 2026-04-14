def backtest(data, strategy):

    balance = 1000
    history = []

    for c in data:

        signal = strategy(c)

        if signal == "BUY":
            balance += 1
        elif signal == "SELL":
            balance -= 1

        history.append(balance)

    return balance, history

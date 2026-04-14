class Account:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.pnl = 0

    def update(self, pnl):
        self.pnl += pnl
        self.balance += pnl


class AccountManager:

    def __init__(self):
        self.accounts = []

    def add(self, acc):
        self.accounts.append(acc)

    def total_balance(self):
        return sum(a.balance for a in self.accounts)

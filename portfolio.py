class Portfolio:

    def __init__(self):
        self.balance = 1000

    def update(self, pnl):
        self.balance += pnl

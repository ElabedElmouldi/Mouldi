class Analytics:

    def __init__(self):
        self.trades = []

    def add(self, pnl):
        self.trades.append(pnl)

    def performance(self):
        return sum(self.trades)

    def win_rate(self):
        wins = len([t for t in self.trades if t > 0])
        total = len(self.trades)
        return (wins / total * 100) if total > 0 else 0

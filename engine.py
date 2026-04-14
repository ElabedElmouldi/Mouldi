from ai.alpha_v2 import alpha_v2
from risk.risk_manager import risk_check
from execution.paper import execute
from portfolio.account_manager import AccountManager, Account
from notifications.telegram import send

def run():
    print("🚀 GOD MODE FUND SYSTEM v2 STARTED")

    manager = AccountManager()
    manager.add(Account("A1", 1000))
    manager.add(Account("A2", 2000))

    while True:

        data = {
            "momentum": 1.2,
            "volatility": 0.8,
            "volume_spike": 1.3
        }

        signal = alpha_v2(data)

        if not risk_check(data, 0.1):
            continue

        for acc in manager.accounts:
            pnl = execute(signal, 0.01)
            acc.update(1 if signal=="BUY" else -1 if signal=="SELL" else 0)

        send(f"Signal: {signal} | Total balance: {manager.total_balance()}")
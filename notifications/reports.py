from .telegram import send

def send_dashboard(balance, pnl, win_rate):

    msg = f"""
📊 *FUND DASHBOARD*

💰 Balance: `{balance:.2f}`
📈 PnL: `{pnl:.2f}`
🎯 Win Rate: `{win_rate:.2f}%`
"""

    send(msg)

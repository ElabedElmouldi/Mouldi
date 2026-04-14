from market import get_market
from brain import ai_score
from strategies import trend_strategy, mean_reversion, breakout
from optimizer import Optimizer
from risk import risk_check
from portfolio import Portfolio
from analytics import Analytics

from notifications.signals import send_signal
from notifications.risk_alerts import send_risk
from notifications.reports import send_dashboard

portfolio = Portfolio()
optimizer = Optimizer()
analytics = Analytics()

def run():

    print("🚀 AI HEDGE FUND v4 STARTED")

    for i in range(200):

        data = get_market()

        if not risk_check(data):
            send_risk(data["volatility"])
            continue

        scores = {
            "AI": ai_score(data),
            "TREND": trend_strategy(data),
            "MEAN": mean_reversion(data),
            "BREAKOUT": breakout(data)
        }

        best = optimizer.best(scores)

        score = scores[best]

        pnl = score * 0.1

        portfolio.update(pnl)
        analytics.add(pnl)

        # إرسال إشارات فقط القوية
        if abs(score) > 2.2:
            send_signal(best, score, portfolio.balance, data)

        # تقرير كل 20 خطوة
        if i % 20 == 0:
            send_dashboard(
                portfolio.balance,
                analytics.performance(),
                analytics.win_rate()
            )

    print("DONE")

if __name__ == "__main__":
    run()

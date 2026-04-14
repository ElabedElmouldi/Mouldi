
from .telegram import send
from .ai_explainer import explain

def send_signal(best, score, balance, data):

    explanation = explain(data, score)

    msg = f"""
📊 *INSTITUTIONAL SIGNAL*

🔥 Strategy: `{best}`
📈 Score: `{score:.2f}`
💰 Balance: `{balance:.2f}`

🧠 AI Insight:
{explanation}
"""

    send(msg)

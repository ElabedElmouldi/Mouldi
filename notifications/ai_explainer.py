def explain(data, score):

    reasons = []

    if data["trend"] > 0:
        reasons.append("📈 Uptrend")

    if data["momentum"] > 1:
        reasons.append("🚀 Strong momentum")

    if data["rsi"] > 50:
        reasons.append("💪 Bullish RSI")

    if data["volume"] > 1.2:
        reasons.append("📊 High volume")

    return "\n".join(reasons)

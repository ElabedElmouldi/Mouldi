
def ai_score(data):

    score = 0

    score += data["trend"] * 2
    score += data["momentum"] * 1.5
    score += (data["rsi"] - 50) / 10
    score += data["volume"]
    score -= data["volatility"]

    return score

def score_coin(c):

    score = 0

    score += c["momentum"] * 30
    score += c["volume"] * 25

    if c["trend_5m"] == "UP" and c["trend_1h"] == "UP":
        score += 20

    if 0.8 < c["volatility"] < 1.5:
        score += 15

    if c["near_resistance"]:
        score += 10

    return score

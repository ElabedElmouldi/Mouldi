
def score_coin(c):

    score = 0

    # Momentum
    score += c["momentum"] * 30

    # Volume spike
    score += c["volume"] * 25

    # Trend alignment (multi timeframe)
    if c["trend_5m"] == "UP" and c["trend_1h"] == "UP":
        score += 20

    # Volatility squeeze (early explosion signal)
    if 0.8 < c["volatility"] < 1.5:
        score += 15

    # Resistance breakout pressure
    if c["near_resistance"]:
        score += 10

    return score

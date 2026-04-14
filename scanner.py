
from scoring import score_coin

def scan_market(coins):

    results = []

    for i in range(0, len(coins), 150):

        batch = coins[i:i+150]

        print(f"🔍 Scanning batch {i//150 + 1}")

        for c in batch:

            score = score_coin(c)

            c["score"] = score

            if score >= 75:
                results.append(c)

    return sorted(results, key=lambda x: x["score"], reverse=True)

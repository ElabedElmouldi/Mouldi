from data import get_symbols, get_data

def scan(engine):

    signals = []

    for s in get_symbols():

        try:
            df = get_data(s)

            result = engine.strategy.generate_signal(df)

            if result["signal"]:

                signals.append({
                    "symbol": s,
                    "price": df['c'].iloc[-1],
                    "score": result["score"]
                })

        except:
            continue

    return signals

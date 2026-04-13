from binance.client import Client
import pandas as pd

client = Client()

def get_symbols():
    tickers = client.get_ticker()
    return [t['symbol'] for t in tickers if t['symbol'].endswith("USDT")]


def get_data(symbol, interval="5m"):
    klines = client.get_klines(symbol=symbol, interval=interval, limit=200)

    df = pd.DataFrame(klines, columns=[
        't','o','h','l','c','v','ct','q','n','tb','tq','ig'
    ])

    df['c'] = df['c'].astype(float)
    df['v'] = df['v'].astype(float)

    return df

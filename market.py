
import random

def get_market():
    return {
        "price": 100 + random.uniform(-2, 2),
        "trend": random.uniform(-1, 1),
        "momentum": random.uniform(-2, 2),
        "rsi": random.randint(20, 80),
        "volatility": random.uniform(0.2, 3),
        "volume": random.uniform(0.5, 2)
    }

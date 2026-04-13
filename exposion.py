from strategy.base import StrategyBase

class ExplosionStrategy(StrategyBase):

    def generate_signal(self, df):

        price_change = (df['c'].iloc[-1] - df['c'].iloc[-5]) / df['c'].iloc[-5]

        vol_avg = df['v'].rolling(20).mean().iloc[-1]

        volume_spike = df['v'].iloc[-1] > vol_avg * 2

        if price_change > 0.02 and volume_spike:

            return {
                "signal": True,
                "score": 0.8
            }

        return {
            "signal": False,
            "score": 0.0
        }

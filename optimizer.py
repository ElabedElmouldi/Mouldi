class Optimizer:

    def best(self, scores):
        return max(scores, key=scores.get)

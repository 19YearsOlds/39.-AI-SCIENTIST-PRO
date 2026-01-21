import numpy as np

class ScoringModel:
    def score(self, hypothesis, experiment_results):
        corr = experiment_results["correlation"]
        novelty = np.random.uniform(0.5, 1.0)
        return 0.6 * abs(corr) + 0.4 * novelty
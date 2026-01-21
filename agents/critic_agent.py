from models.scoring_model import ScoringModel

class CriticAgent:
    def __init__(self):
        self.scorer = ScoringModel()

    def evaluate(self, hypothesis, experiment_results):
        return self.scorer.score(hypothesis, experiment_results)
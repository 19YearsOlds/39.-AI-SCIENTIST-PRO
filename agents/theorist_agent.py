from models.reasoning_model import ReasoningModel

class TheoristAgent:
    def __init__(self):
        self.model = ReasoningModel()

    def generate(self, claims, results):
        return self.model.propose(claims, results)
from core.hypothesis import Hypothesis

class ResearchLoop:
    def iterate(self, theorist, critic, claims, results):
        hypothesis = theorist.generate(claims, results)
        score = critic.evaluate(hypothesis, results["linear"])
        return Hypothesis(hypothesis, score)
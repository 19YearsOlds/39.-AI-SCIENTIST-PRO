from agents.reader_agent import ReaderAgent
from agents.experiment_agent import ExperimentAgent
from agents.theorist_agent import TheoristAgent
from agents.critic_agent import CriticAgent
from core.research_loop import ResearchLoop
from utils.logger import log

class AIScientist:
    def __init__(self):
        self.reader = ReaderAgent()
        self.experimenter = ExperimentAgent()
        self.theorist = TheoristAgent()
        self.critic = CriticAgent()
        self.loop = ResearchLoop()

    def run(self, paper_text):
        log("Extracting claims...")
        claims = self.reader.read(paper_text)

        log("Running experiments...")
        results = self.experimenter.run_all()

        log("Research iteration...")
        hypothesis = self.loop.iterate(
            self.theorist, self.critic, claims, results
        )

        return hypothesis
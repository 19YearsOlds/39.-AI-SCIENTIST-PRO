from simulations.linear_dynamics import run as linear
from simulations.nonlinear_dynamics import run as nonlinear

class ExperimentAgent:
    def run_all(self):
        return {
            "linear": linear(),
            "nonlinear": nonlinear()
        }
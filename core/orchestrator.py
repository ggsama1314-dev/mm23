from agents.analyzer import AnalyzerAgent
from agents.reviewer import ReviewerAgent
from agents.optimizer import OptimizerAgent
from agents.tester import TesterAgent

class Orchestrator:
    def __init__(self):
        self.agents = [
            AnalyzerAgent("Analyzer"),
            ReviewerAgent("Reviewer"),
            OptimizerAgent("Optimizer"),
            TesterAgent("Tester")
        ]

    def run(self, code):
        context = {"code": code}

        for agent in self.agents:
            context = agent.run(context)

        return context

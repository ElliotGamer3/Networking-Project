from src.graph.graph import Graph
from src.network.network import Network
from src.graph.node.node import Node
from src.graph.edge.edge import Edge
from src.simulation.costClass import NonPredictiveScenario


class NonPredictiveTravelerScenario:
    def __init__(self, presetNetwork) -> None:
        self.network = presetNetwork.network
        self.travelers = presetNetwork.travelers
        self.scenario = NonPredictiveScenario(self.network, self.travelers, 3)

    def run(self):
        self.scenario.run()

    def getLogs(self):
        return self.scenario.getLogs()
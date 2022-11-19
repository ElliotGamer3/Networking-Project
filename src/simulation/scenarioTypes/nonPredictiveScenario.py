from src.network.network import Network
from src.graph.node.node import Node
from src.simulation.travelerTypes.nonTraveler import NonTraveler
from src.simulation.costClass import CostClass


class NonPredictiveScenario:
    def __init__(self, network: Network, travelerPaths: list[list[Node]], iterations: int = None) -> None:
        if iterations is None:
            iterations = 1
        self.iterations = iterations
        self.network = network
        self.travelers = []
        for path in travelerPaths:
            traveler = NonTraveler(self.network, path)
            self.travelers.append(traveler)
        self.costClass = CostClass(self.network, self.travelers)

    def run(self) -> None:
        # create an instance of the travel class
        # perform 10 ticks of the simulation
        for i in range(self.iterations):
            self.costClass.tick()
            # print out the logs
        self.costClass.printLogs()

    def getLogs(self) -> dict[str, list]:
        return self.costClass.getLogs()

    def printLogs(self) -> None:
        for log in self.costClass.getLogs():
            print(log)

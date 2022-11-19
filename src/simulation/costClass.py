from src.graph.graph import Graph
from src.graph.node.node import Node
from src.graph.edge.edge import Edge
from src.graph.graphable.graphable import Graphable
from src.network.network import Network
from src.simulation.traveler import Traveler
from src.simulation.genericNetwork import GenericNetworkWithTravelers


class CostClass(GenericNetworkWithTravelers):
    def __init__(self, network: Network, travelers: list[Traveler]) -> None:
        # if the network is not given, create a new one
        super().__init__(network, travelers)
        self.complete_system_cost_log = []
        self.system_cost_log = []
        self.total_ticks = 0

    def log(self) -> None:
        # log the complete system cost
        self.complete_system_cost_log.append(
            self.network.getCompleteSystemCost())
        # log the system cost
        self.system_cost_log.append(self.network.getSystemCost())

    def printLogs(self) -> None:
        # print out all the logs for the travelers
        for tick in range(self.total_ticks):
            print(f"Tick: {str(tick)}")

            print(
                f"Complete System Cost: {str(self.complete_system_cost_log[tick])}"
            )

            print(f"System Cost: {str(self.system_cost_log[tick])}")
            print("")

    def getLogs(self) -> dict[str, list]:
        return {
            "complete_system_cost_log": self.complete_system_cost_log,
            "system_cost_log": self.system_cost_log,
        }

    def tick(self) -> None:
        self.total_ticks += 1
        for traveler in self.travelers:
            traveler.goToNext()
        self.log()


class Scenario:
    def __init__(self, network: Network, travelerPaths: list[list[Node]], iterations: int = None) -> None:
        if iterations is None:
            iterations = 1
        self.iterations = iterations
        self.network = network
        self.travelers = []
        for path in travelerPaths:
            traveler = Traveler(self.network, path)
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

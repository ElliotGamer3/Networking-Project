from src.graph.graph import Graph
from src.graph.node.node import Node
from src.graph.edge.edge import Edge
from src.graph.graphable.graphable import Graphable
from src.network.network import Network
from src.simulation.travelerTypes.traveler import Traveler
from src.simulation.travelerTypes.nonTraveler import NonTraveler
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

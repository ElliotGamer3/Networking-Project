from src.graph.graph import Graph
from src.graph.node.node import Node
from src.graph.edge.edge import Edge
from src.graph.graphable.graphable import Graphable
from src.network.network import Network
from src.simulation.traveler import Traveler

# this class represents a simple network with 3 nodes and 2 edges
# the goal of the network is to travel from node1 to node3


class GenericNetwork:
    def __init__(self, network) -> None:
        self.network = network


class SimpleNetwork(GenericNetwork):
    def __init__(self) -> None:
        # create the nodes
        self.node1 = Node("node1", 0.0)
        self.node2 = Node("node2", 0.0)
        self.node3 = Node("node3", 0.0)
        # create the edge between the nodes with a cost of 1
        self.edge1 = Edge(self.node1, self.node2, 1, "edge1", 1.0)
        self.edge2 = Edge(self.node2, self.node3, 1, "edge2", 2.0)
        # save the network name
        self.name = "simple_network"
        # create the network with the nodes and edges
        self.network = Network(
            [self.node1, self.node2, self.node3, self.edge1, self.edge2])


class TravelClass(SimpleNetwork):
    def __init__(self, start_location=None, end_location=None) -> None:
        # if the network is not given, create a new one
        super().__init__()

        self.start_location = start_location
        self.end_location = end_location
        if start_location is None:
            self.start_location = self.network.getNodes()[0]
        if end_location is None:
            self.end_location = self.network.getNodes()[-1]
        self.travelers = []
        self.last_travel_paths = []
        self.interaction_cost_log = []
        self.complete_system_cost_log = []
        self.system_cost_log = []
        self.travel_path_log = []
        self.total_ticks = 0
        self.traveled = False

    def log(self) -> None:
        self.interaction_cost_log.append(
            self.network.getInteractionCosts(self.last_travel_paths))
        # log the complete system cost
        self.complete_system_cost_log.append(
            self.network.getCompleteSystemCost())
        # log the system cost
        self.system_cost_log.append(self.network.getSystemCost())

    def printLogs(self) -> None:
        # print out all the logs for the travelers
        for tick in range(self.total_ticks):
            print("Tick: " + str(tick))
            print("Interaction Cost: " + str(self.interaction_cost_log[tick]))
            print("Complete System Cost: " +
                  str(self.complete_system_cost_log[tick]))
            print("System Cost: " + str(self.system_cost_log[tick]))
            print("")

    def getLogs(self) -> dict[str, list]:
        return {
            "interaction_cost_log": self.interaction_cost_log,
            "complete_system_cost_log": self.complete_system_cost_log,
            "system_cost_log": self.system_cost_log,
        }


# travel class that travels to all nodes in the network
class EveryNodeTravel(TravelClass):

    def __init__(self, start_location=None, end_location=None) -> None:
        super().__init__(start_location, end_location)

    def tick(self) -> list[list[Graphable]]:
        self.total_ticks += 1
        # below is the travel method specific to this class
        # create a list of traveler's travel paths
        if self.start_location is not None and self.end_location is not None:
            if self.start_location == self.end_location:
                self.traveled = True
                return []
            if self.traveled:
                return []

        traveler_paths = []
        new_travelers = [EveryNodeTravel(self.node1, self.node2)]
        # perform a tick for each traveler and save their travel path
        for traveler in self.travelers:
            self.travelers.remove(traveler)
            if traveler.traveled:
                continue
            for neighbor in self.network.getNeighbors(traveler.start_location):
                subTraveler = EveryNodeTravel(
                    neighbor, traveler.end_location)
                new_travelers.append(subTraveler)
            for subTraveler in new_travelers:
                for subPath in subTraveler.tick():
                    traveler_paths.append(subPath)
                    print("Traveler: " + traveler.name +
                          " traveled to: " + neighbor.name)
                    print("Traveler: path: " + str(traveler_paths[-1]))
        self.travelers = new_travelers
        self.last_travel_paths = traveler_paths
        self.log()
        return traveler_paths


class EveryNodeTravelerScenario:
    def __init__(self, iterations=None) -> None:
        if iterations is None:
            iterations = 1
        self.iterations = iterations
        self.travel = EveryNodeTravel()
        self.network = self.travel.network

    def run(self) -> None:
        # create an instance of the travel class
        # perform 10 ticks of the simulation
        for i in range(self.iterations):
            self.travel.tick()

        # print out the logs
        self.travel.printLogs()

    def getLogs(self) -> dict[str, list]:
        return self.travel.getLogs()

    def printLogs(self) -> None:
        for log in self.travel.getLogs():
            print(log)

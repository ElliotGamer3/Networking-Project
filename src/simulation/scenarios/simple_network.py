from src.graph.graph import Graph
from src.graph.node.node import Node
from src.graph.edge.edge import Edge
from src.graph.graphable.graphable import Graphable
from src.network.network import Network
from src.simulation.traveler import Traveler

# this class represents a simple network with 3 nodes and 2 edges
# the goal of the network is to travel from node1 to node3


class SimpleNetwork:
    def __init__(self) -> None:
        # create the nodes
        self.node1 = Node("node1")
        self.node2 = Node("node2")
        # create the edge between the nodes with a cost of 1
        self.edge = Edge("edge", self.node1, self.node2, 1.0)
        # save the network name
        self.name = "simple_network"
        # create the network with the nodes and edges
        self.network = Network([self.node1, self.node2, self.edge])
        self.travelers = [Traveler(
            self.network, self.travel_method1, "traveler1", self.node1, self.node2)]

    # function for performing a tick of the simulation
    def tick(self) -> None:
        # create a list of traveler's travel paths
        traveler_paths = []
        # perform a tick for each traveler and save their travel path
        for traveler in self.travelers:
            traveler_paths.append(traveler.travel())
        self.network.updateNetwork(self.network, traveler_paths)

# brute force method of travel that travels to all nodes neighboring the current node until it reaches the end destination
# nodes can be revisited a maximum of 2 times before the traveler gives returns a path
# the path may not contain the end destination if the traveler is unable to reach it but
# is used to determine the cost of the path


def travelMethod1(network, start_destination, end_destination):
    pass

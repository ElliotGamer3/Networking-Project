from uuid import uuid4
from src.network.network import Network
from src.graph.node.node import Node
from src.graph.edge.edge import Edge
from src.graph.graphable.graphable import Graphable
from src.graph.graph import Graph
# this class represents a traveler in the simulation
# the traveler will travel from one node to another on a network using a method of travel
# it can provide its travel path


class Traveler:
    def __init__(self, network: Network, name: str = None, start_location: Node = None, end_location: Node = None) -> None:
        self._name = name
        self._guid = str(uuid4())  # Generate a random guid
        self._start_location = start_location
        self._end_location = end_location
        self._network = network
        self.travel_path = [self.start_location]
        self.traveled = False  # flag to indicate if the traveler has finished traveling

    @property
    def name(self) -> str:
        if self._name == None:
            self._name = self._guid
        return self._name

    @property
    def guid(self) -> str:
        return self._guid

    @property
    def start_location(self) -> Node:
        if self._start_location == None:
            self._start_location = self._network.nodes[0]
        return self._start_location

    @property
    def end_location(self) -> Node:
        if self._end_location == None:
            self._end_location = self._network.nodes[-1]
        return self._end_location

    @property
    def network(self) -> Network:
        if self._network == None:
            raise Exception("No network has been set for the traveler")
        return self._network

    # returns the current travel path of the traveler as a list of list of nodes
    def getTravelPath(self) -> list[Node]:
        return self.travel_path

    # travels to the given node returns true if the traveler has reached the end destination
    def travelTo(self, node: Node) -> list[Node]:
        # check if the node is in the network
        if node not in self.network.getNodes():
            raise Exception("The node is not in the network")
        if node not in self.network.getNeighbors(self.start_location):
            raise Exception(
                "The node is not a neighbor of the last node in the travel path")
        # get the nodes that the traveler can travel to from the current location
        neighbors = self.network.getNeighbors(self.travel_path[-1])
        self.travel_path.append(node)  # add the node to the travel path
        self._start_location = node  # set the start location to the node
        # check if the traveler has reached the end destination or if there are no more edges to travel to
        if node == self.end_location or self.network.getEdgesFromNode(node) == []:
            self.traveled = True
        print(self.travel_path)
        return self.travel_path

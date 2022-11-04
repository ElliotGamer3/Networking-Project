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
    def __init__(self, network: Network, travel_method: function, name: str = None, start_location: str = None, end_destination: str = None) -> None:
        self._name = name
        self._guid = str(uuid4())  # Generate a random guid
        self._start_location = start_location
        self._end_destination = end_destination
        self._network = network
        self._travel_method = travel_method
        self.travel_path = []

    @property
    def name(self) -> str:
        if self._name == None:
            self._name = self._guid
        return self._name

    @property
    def guid(self) -> str:
        return self._guid

    @property
    def start_location(self) -> str:
        if self._start_location == None:
            self._start_location = self._network.nodes[0]
        return self._start_location

    @property
    def end_destination(self) -> str:
        if self._end_destination == None:
            self._end_destination = self._network.nodes[-1]
        return self._end_destination

    @property
    def network(self) -> Network:
        if self._network == None:
            raise Exception("No network has been set for the traveler")
        return self._network

    @property
    def travel_method(self) -> function:
        if self._travel_method == None:
            raise Exception("No travel method has been set for the traveler")
        return self._travel_method

    # returns the current travel path of the traveler
    def getTravelPath(self) -> list[Node]:
        return self.travel_path

    # performs a tick of the simulation for the traveler using the given method of travel
    def travel(self) -> None:
        return self.travel_method(self.network, self.start_location, self.end_destination)

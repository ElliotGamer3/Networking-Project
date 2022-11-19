from random import random
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
    def __init__(self, network: Network, travelPath: list[Node] = None, name: str = None) -> None:

        self._guid = str(uuid4())  # Generate a random guid
        self._name = name
        self._network = network
        self._travelPath = travelPath
        if self._travelPath is None:
            self._travelPath = [self._network.getNodes()[0]]
        self._start_location = self._travelPath[0]
        self._end_location = self._travelPath[-1]
        self._current_location = self._travelPath[0]
        if len(self._travelPath) <= 1:
            self._traveled = True
            self._next_location = None
        else:
            self.traveled = False  # flag to indicate if the traveler has finished traveling
            self._next_location = self._travelPath[1]
        self._last_location = None

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
        return self._start_location

    @property
    def end_location(self) -> Node:
        return self._end_location

    @property
    def last_location(self) -> Node:
        return self._last_location

    @property
    def current_location(self) -> Node:
        return self._current_location

    @property
    def next_location(self) -> Node:
        return self._next_location

    @property
    def travelPath(self) -> list[Node]:
        return self._travelPath

    @property
    def network(self) -> Network:
        if self._network == None:
            raise Exception("No network has been set for the traveler")
        return self._network

    def goToNext(self) -> None:
        if self.travelPath == None or self.travelPath == []:
            self.traveled = True
            self._next_location = None
            return
        if self.traveled:
            self._next_location = None
            return
        if self.next_location == None:
            self.traveled = True
            return
        if self.current_location == self.end_location and self.next_location == None or self.travelPath == []:
            self.traveled = True
            self._next_location = None
            return
        # update the last location
        self._last_location = self.current_location
        # update the current location
        self._current_location = self.next_location
        # update the next location
        if len(self.travelPath) >= 1:
            self._next_location = self.travelPath.pop(0)
        else:
            self.travelPath = []
            self._next_location = None
            self.traveled = True
            return
        self.travelTo(self.next_location)

    # looks at the possible paths and assigns a score to each one
    # the last location the traveler was at is given the lowest score
    # the next location is given the highest score
    # and the locations adjacent to the next location are given the next highest scores
    # in a true application of the algorithm, the scores would be based on
    # factors such as the speed of the traveler the direction of the traveler and other factors that can be determined using passive RF tracking data
    # however for simplicity, the scores are as follows:
    # last location: 0.02
    # other locations: 0.14
    # next location: 0.70
    # updates the edges in the network to reflect the traveler's path

    def updateScores(self) -> None:
        # from the current location, get the neighbors
        neighbors = self.network.getNeighbors(self.current_location)
        # get the next location
        next_location = self.next_location
        for neighbor in neighbors:
            if neighbor == next_location:
                # get the edge between the current location and the next location
                edge = self.network.getEdgeByNodes(
                    self.current_location, next_location)
                # set the edge score to 0.7
                addToScore = 0.7
            elif neighbor == self.last_location:
                # get the edge between the current location and the last location
                edge = self.network.getEdgeByNodes(
                    self.current_location, self.last_location)
                # set the edge score to 0.02
                addToScore = 0.02
            else:
                # get the edge between the current location and the neighbor
                edge = self.network.getEdgeByNodes(
                    self.current_location, neighbor)
                # set the edge score to 0.14
                addToScore = 0.14
            currentEdgeCost = self.network.getEdgeCost(
                edge)  # get the current cost of the edge
            newEdgeCost = currentEdgeCost + addToScore  # add the score to the current cost
            # set the new cost of the edge
            self.network.setEdgeCost(edge, newEdgeCost)

    def travelTo(self, node: Node) -> None:
        # check if the node is in the network
        if node not in self.network.getNodes():
            raise Exception("The node is not in the network")
        if node not in self.network.getNeighbors(self.current_location):
            raise Exception(
                "The node is not a neighbor of the current location")
        self.updateScores()

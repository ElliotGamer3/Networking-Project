#unittests for the traveler class
import unittest
from src.simulation.traveler import Traveler
from src.network.network import Network
from src.graph.node.node import Node
from src.graph.edge.edge import Edge
from src.graph.graphable.graphable import Graphable
from src.graph.graph import Graph

def travel_method(network: Network, current_node:Node, destination_node:Node, path:list[Node]=None) -> None:
    if path == None:
        path = []
    path.append(current_node)
    if current_node == destination_node:
        return path
    for edge in network.getEdgesFromNode(current_node):
        if edge.node2 not in path:
            path.append(travel_method(network, edge.node2, destination_node, path))
            return path


class TestTravelerFunctionsBase(unittest.TestCase):
    def setUp(self) -> None:
        self.node1 = Node("node1")
        self.node2 = Node("node2")
        self.node3 = Node("node3")
        self.edge1 = Edge(self.node1, self.node2, 1, "edge1")
        self.edge2 = Edge(self.node2, self.node3, 1, "edge2")
        self.edges = [self.edge1, self.edge2]
        self.nodes = [self.node1, self.node2, self.node3]
        self.graph1 = Graph(self.edges)
        self.graph2 = Graph(self.nodes)
        self.graph3 = Graph([])
        self.network = Network(self.edges+self.nodes)
        #the travel function creates a new traveler for all neighbors of the current node and then calls the travel method on the new traveler
        #this continues until the traveler reaches the destination node or there are no more neighbors to travel to that have not been visited
        self.traveler_method = travel_method
        self.traveler = Traveler(self.network, self.traveler_method, "traveler", self.node1.name, self.node3.name)
        return super().setUp()

    def tearDown(self) -> None:
        self.traveler = None
        self.network = None
        self.graph3 = None
        self.graph2 = None
        self.graph1 = None
        self.nodes = None
        self.edges = None
        self.edge2 = None
        self.edge1 = None
        self.node3 = None
        self.node2 = None
        self.node1 = None
        return super().tearDown()

#test the travel method
class TestTravel(TestTravelerFunctionsBase):
    def runTest(self):
        self.traveler.travel()
        self.assertEqual(self.traveler.travel(), [self.node1.name])
        
        

#test the get path method
class TestGetTravelPath(TestTravelerFunctionsBase):
    def runTest(self):
        self.assertEqual(self.traveler.getTravelPath(), [])
        self.traveler.travel()
        self.assertEqual(self.traveler.getTravelPath(), [self.node1.name])
        self.traveler.travel()
        self.assertEqual(self.traveler.getTravelPath(), [self.node1.name, self.node2.name])
        self.traveler.travel()
        self.assertEqual(self.traveler.getTravelPath(), [self.node1.name, self.node2.name, self.node3.name])
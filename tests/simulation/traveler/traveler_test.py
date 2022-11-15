#unittests for the traveler class
import unittest
from src.simulation.traveler import Traveler
from src.network.network import Network
from src.graph.node.node import Node
from src.graph.edge.edge import Edge
from src.graph.graphable.graphable import Graphable
from src.graph.graph import Graph

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
        
        self.traveler = Traveler(self.network, "traveler", self.node1, self.node3)
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

#test the travelTo method
class TestTravelerTravelTo(TestTravelerFunctionsBase):
    def runTest(self):
        self.traveler.travelTo(self.node2)
        self.assertEqual(self.traveler.travel_path, [self.node1, self.node2])
        self.traveler.travelTo(self.node3)
        self.assertEqual(self.traveler.travel_path, [self.node1, self.node2, self.node3])
        self.assertTrue(self.traveler.traveled)

#test the getTravelPath method
class TestTravelerGetTravelPath(TestTravelerFunctionsBase):
    def runTest(self):
        self.assertEqual(self.traveler.getTravelPath(), [self.node1])
        self.traveler.travelTo(self.node2)
        self.assertEqual(self.traveler.getTravelPath(), [self.node1, self.node2])
        self.traveler.travelTo(self.node3)
        self.assertEqual(self.traveler.getTravelPath(), [self.node1, self.node2, self.node3])
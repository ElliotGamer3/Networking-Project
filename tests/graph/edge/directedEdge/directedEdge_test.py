#unit tests for directedEdge.py
import unittest
from src.graph.edge.directedEdge import DirectedEdge
from src.graph.node.node import Node
class TestDirectedEdgeFunctionsBase(unittest.TestCase):
    def setUp(self) -> None:
        self.node1 = Node("node1")
        self.node2 = Node("node2")
        self.edge = DirectedEdge(self.node1, self.node2, 1, "edge")
        return super().setUp()
    def tearDown(self) -> None:
        self.edge = None
        self.node2 = None
        self.node1 = None
        return super().tearDown()



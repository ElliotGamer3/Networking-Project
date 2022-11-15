#unit tests for the edge class
import unittest
from src.graph.edge.edge import Edge
from src.graph.node.node import Node
class TestEdgeFunctionsBase(unittest.TestCase):
    def setUp(self) -> None:
        self.node1 = Node("node1")
        self.node2 = Node("node2")
        self.edge = Edge(self.node1, self.node2, 1, "edge")
        return super().setUp()
    def tearDown(self) -> None:
        self.edge = None
        self.node2 = None
        self.node1 = None
        return super().tearDown()

class TestToString(TestEdgeFunctionsBase):
    def runTest(self):
        self.assertEqual(self.edge.__str__(), "edge: node1 -> node2")

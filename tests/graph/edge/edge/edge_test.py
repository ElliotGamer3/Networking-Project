#unit tests for the edge class
import unittest
from src.graph.edge.edge import Edge
from src.graph.node.node import Node
class TestEdgeFunctionsBase(unittest.TestCase):
    def setUp(self) -> None:
        self.node1 = Node("node1")
        self.node2 = Node("node2")
        self.edge = Edge(self.node1, self.node2, 0, "edge")
        return super().setUp()
    def tearDown(self) -> None:
        self.edge = None
        self.node2 = None
        self.node1 = None
        return super().tearDown()

#Test that the node1 and node2 are set correctly
class TestEdgeNode1(TestEdgeFunctionsBase):
    def runTest(self):
        self.assertEqual(self.edge.node1, self.node1)
    
class TestEdgeNode2(TestEdgeFunctionsBase):
    def runTest(self):
        self.assertEqual(self.edge.node2, self.node2)

#Test that the direction is set correctly
class TestEdgeDirection(TestEdgeFunctionsBase):
    def runTest(self):
        self.assertEqual(self.edge.direction, 0)
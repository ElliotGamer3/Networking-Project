#unitTests for the edge functions in the graph class
import unittest
from src.graph.edge.edge import Edge
from src.graph.node.node import Node
from src.graph.graph import Graph
class TestGraphEdgeFunctionsBase(unittest.TestCase):
    def setUp(self) -> None:
        self.node1 = Node("node1")
        self.node2 = Node("node2")
        self.node3 = Node("node3")
        self.edge1 = Edge(self.node1, self.node2, 1, "edge1")
        self.edge2 = Edge(self.node2, self.node3, 1, "edge2")
        self.edge3 = Edge(self.node3, self.node1, 1, "edge3")
        self.edge4 = Edge(self.node1, self.node3, 1, "edge4")
        self.edges = [self.edge1, self.edge2, self.edge3]
        self.nodes = [self.node1, self.node2, self.node3]
        self.graph = Graph(self.edges)
        return super().setUp()
    def tearDown(self) -> None:
        self.graph = None
        self.nodes = None
        self.edges = None
        self.edge4 = None
        self.edge3 = None
        self.edge2 = None
        self.edge1 = None
        self.node3 = None
        self.node2 = None
        self.node1 = None
        return super().tearDown()

#test the addEdge method
class TestAddEdge(TestGraphEdgeFunctionsBase):
    def runTest(self):
        self.graph.addEdge(self.edge4)
        self.assertEqual(self.graph.getEdges(), self.edges+[self.edge4])

#test the removeEdge method
class TestRemoveEdge(TestGraphEdgeFunctionsBase):
    def runTest(self):
        self.graph.removeEdge(self.edge1)
        self.assertEqual(self.graph.getEdges(), [self.edge2, self.edge3])

#test the getEdge method
class TestGetEdge(TestGraphEdgeFunctionsBase):
    def runTest(self):
        self.assertEqual(self.graph.getEdge(self.edge1.name), self.edge1)
        self.assertEqual(self.graph.getEdge(self.edge2.name), self.edge2)
        self.assertEqual(self.graph.getEdge(self.edge3.name), self.edge3)

#test the getEdgeByGUID method
class TestGetEdgeByGUID(TestGraphEdgeFunctionsBase):
    def runTest(self):
        self.assertEqual(self.graph.getEdgeByGUID(self.edge1.guid), self.edge1)
        self.assertEqual(self.graph.getEdgeByGUID(self.edge2.guid), self.edge2)
        self.assertEqual(self.graph.getEdgeByGUID(self.edge3.guid), self.edge3)

#test the getEdgeByEdge method
class TestGetEdgeByEdge(TestGraphEdgeFunctionsBase):
    def runTest(self):
        self.assertEqual(self.graph.getEdgeByEdge(self.edge1), self.edge1)
        self.assertEqual(self.graph.getEdgeByEdge(self.edge2), self.edge2)
        self.assertEqual(self.graph.getEdgeByEdge(self.edge3), self.edge3)

#test the getEdgeByNodes method
class TestGetEdgeByNodes(TestGraphEdgeFunctionsBase):
    def runTest(self):
        self.assertEqual(self.graph.getEdgeByNodes(self.node1, self.node2), self.edge1)
        self.assertEqual(self.graph.getEdgeByNodes(self.node2, self.node3), self.edge2)
        self.assertEqual(self.graph.getEdgeByNodes(self.node3, self.node1), self.edge3)

#test the getEdges method
class TestGetEdges(TestGraphEdgeFunctionsBase):
    def runTest(self):
        self.assertEqual(self.graph.getEdges(), self.edges)


#test the getEdgesFromNode method
class TestGetEdgesFromNode(TestGraphEdgeFunctionsBase):
    def runTest(self):
        self.assertEqual(self.graph.getEdgesFromNode(self.node1), [self.edge1])
        self.assertEqual(self.graph.getEdgesFromNode(self.node2), [self.edge2])
        self.assertEqual(self.graph.getEdgesFromNode(self.node3), [self.edge3])

#unit tests for the node functions in the Graph class

import unittest
from graph.graph import Graph
from graph.node.node import Node

class TestNodeFunctionsBase(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = Graph()
        self.node = Node()
        return super().setUp()

    def tearDown(self) -> None:
        self.graph = None
        self.node = None
        return super().tearDown()

class TestAddNode(TestNodeFunctionsBase):
    def runTest(self):
        self.graph.addNode(self.node)
        self.assertEqual(self.graph.nodes[0], self.node)

class TestRemoveNode(TestNodeFunctionsBase):
    def runTest(self):
        self.graph.addNode(self.node)
        self.assertEqual(self.graph.removeNode(self.node), self.node)
        self.assertEqual(self.graph.nodes, [])

class TestGetNodes(TestNodeFunctionsBase):
    def runTest(self):
        self.graph.addNode(self.node)
        self.assertEqual(self.graph.getNodes(), [self.node])
    
class TestGetNode(TestNodeFunctionsBase):
    def runTest(self):
        self.graph.addNode(self.node)
        self.assertEqual(self.graph.getNode(self.node.name), self.node)
        self.assertEqual(self.graph.getNode(self.node.guid), self.node)

class TestGetNodeByGUID(TestNodeFunctionsBase):
    def runTest(self):
        self.graph.addNode(self.node)
        self.assertEqual(self.graph.getNodeByGUID(self.node.guid), self.node)
    
class TestNodeFunctions(unittest.TestSuite):
    def __init__(self):
        super().__init__()
        self.addTest(TestAddNode())
        self.addTest(TestRemoveNode())
        self.addTest(TestGetNodes())
        self.addTest(TestGetNode())
        self.addTest(TestGetNodeByGUID())
    
if __name__ == "__main__":
    unittest.main()
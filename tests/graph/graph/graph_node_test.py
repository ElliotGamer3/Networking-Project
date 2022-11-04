# unit tests for the node functions in the Graph class

import unittest
from src.graph.graph import Graph
from src.graph.node.node import Node


class TestNodeFunctionsBase(unittest.TestCase):
    def setUp(self) -> None:
        self.node = Node("testNode")
        self.graph = Graph()
        return super().setUp()

    def tearDown(self) -> None:
        self.graph = None
        self.node = None
        return super().tearDown()


class TestAddNode(TestNodeFunctionsBase):
    def runTest(self):
        self.graph.addNode(self.node)
        # check that the node was added to the graph
        self.assertIn(("node", self.node), self.graph.graph.values())


class TestRemoveNode(TestNodeFunctionsBase):
    def runTest(self):
        self.graph.addNode(self.node)
        self.assertEqual(self.graph.removeNode(self.node), ("node", self.node))


class TestGetNodes(TestNodeFunctionsBase):
    def runTest(self):
        self.graph.addNode(self.node)
        self.assertEqual(self.graph.getNodes(), [self.node])


class TestGetNode(TestNodeFunctionsBase):
    def runTest(self):
        self.graph.addNode(self.node)
        self.assertEqual(self.graph.getNode(self.node.name), self.node)


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

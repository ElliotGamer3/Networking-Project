import unittest
from src.graph.node.node import Node


class TestNodeFunctionsBase(unittest.TestCase):
    def setUp(self) -> None:
        self.node = Node("testNode",)
        return super().setUp()

    def tearDown(self) -> None:
        self.node = None
        return super().tearDown()


class TestGetJSON(TestNodeFunctionsBase):
    def runTest(self):
        self.assertEqual(self.node.getJSON(), {
                         "guid": self.node.guid, "name": self.node.name, "type": self.node.type, "cost": 0})

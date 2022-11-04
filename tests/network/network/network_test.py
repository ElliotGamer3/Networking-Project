# the unit tests for the network class

import unittest
from src.network.network import Network
from src.graph.node.node import Node
from src.graph.edge.edge import Edge


class TestNetworkFunctionsBase(unittest.TestCase):
    def setUp(self) -> None:
        self.node1 = Node("testNode1", cost=0)
        self.node2 = Node("testNode2", cost=0)
        self.edge = Edge(self.node1, self.node2, direction=0,
                         name="testEdge", cost=1)
        # have to add to network to test here
        self.network = Network([self.node1, self.node2, self.edge])
        return super().setUp()

    def tearDown(self) -> None:
        self.network = None
        self.edge = None
        self.node2 = None
        self.node1 = None
        return super().tearDown()


class TestSetNodeCost(TestNetworkFunctionsBase):
    def runTest(self):
        self.network.setNodeCost(self.node1, 5.0)
        self.assertEqual(self.network.node_costs[self.node1.guid], 5.0)


class TestSetNodeCostByGUID(TestNetworkFunctionsBase):
    def runTest(self):
        self.network.setNodeCostByGUID(self.node1.guid, 5)
        self.assertEqual(self.network.node_costs[self.node1.guid], 5)


class TestSetNodeCostByName(TestNetworkFunctionsBase):
    def runTest(self):
        self.network.setNodeCostByName(self.node1.name, 5)
        self.assertEqual(self.network.node_costs[self.node1.guid], 5)


class TestSetEdgeCost(TestNetworkFunctionsBase):
    def runTest(self):
        self.network.setEdgeCost(self.edge, 5)
        self.assertEqual(self.network.edge_costs[self.edge.guid], 5)


class TestSetEdgeCostByGUID(TestNetworkFunctionsBase):
    def runTest(self):
        self.network.setEdgeCostByGUID(self.edge.guid, 5)
        self.assertEqual(self.network.edge_costs[self.edge.guid], 5)


class TestSetEdgeCostByName(TestNetworkFunctionsBase):
    def runTest(self):
        self.network.setEdgeCostByName(self.edge.name, 5)
        self.assertEqual(self.network.edge_costs[self.edge.guid], 5)


class TestGetNodeCost(TestNetworkFunctionsBase):
    def runTest(self):
        self.network.setNodeCost(self.node1, 5)  # tested above
        self.assertEqual(self.network.getNodeCost(self.node1),
                         self.network.node_costs[self.node1.guid])


class TestGetNodeCostByGUID(TestNetworkFunctionsBase):
    def runTest(self):
        self.network.setNodeCost(self.node1, 5)  # tested above
        self.assertEqual(self.network.getNodeCostByGUID(
            self.node1.guid), self.network.node_costs[self.node1.guid])


class TestGetNodeCostByName(TestNetworkFunctionsBase):
    def runTest(self):
        self.network.setNodeCost(self.node1, 5)  # tested above
        self.assertEqual(self.network.getNodeCostByName(
            self.node1.name), self.network.node_costs[self.node1.guid])


class TestGetEdgeCost(TestNetworkFunctionsBase):
    def runTest(self):
        self.network.setEdgeCost(self.edge, 5)  # tested above
        self.assertEqual(self.network.getEdgeCost(self.edge),
                         self.network.edge_costs[self.edge.guid])


class TestGetEdgeCostByGUID(TestNetworkFunctionsBase):
    def runTest(self):
        self.network.setEdgeCost(self.edge, 5)  # tested above
        self.assertEqual(self.network.getEdgeCostByGUID(
            self.edge.guid), self.network.edge_costs[self.edge.guid])


class TestGetEdgeCostByName(TestNetworkFunctionsBase):
    def runTest(self):
        self.network.setEdgeCost(self.edge, 5)  # tested above
        self.assertEqual(self.network.getEdgeCostByName(
            self.edge.name), self.network.edge_costs[self.edge.guid])


class TestReset(TestNetworkFunctionsBase):
    def runTest(self):
        self.network.reset()
        # check that all costs are equal to the node/edge's default cost
        for node in self.network.getNodes():
            self.assertEqual(self.network.node_costs[node.guid], node.cost)
        for edge in self.network.getEdges():
            self.assertEqual(self.network.edge_costs[edge.guid], edge.cost)

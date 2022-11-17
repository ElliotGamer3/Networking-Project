# the unit tests for the network class

import unittest
from src.network.network import Network
from src.graph.node.node import Node
from src.graph.edge.edge import Edge


class TestNetworkFunctionsBase(unittest.TestCase):
    def setUp(self) -> None:
        self.node1 = Node("testNode1", cost=0.0)
        self.node2 = Node("testNode2", cost=0.0)
        self.edge = Edge(self.node1, self.node2, direction=0,
                         name="testEdge", cost=1.0)
        # have to add to network to test here
        self.network = Network([self.node1, self.node2, self.edge])
        return super().setUp()

    def tearDown(self) -> None:
        self.network = None
        self.edge = None
        self.node2 = None
        self.node1 = None
        return super().tearDown()


class TestNetworkSetNodeCost(TestNetworkFunctionsBase):
    def runTest(self):
        self.network.setNodeCost(self.node1, 5.0)
        self.assertEqual(self.network.node_costs[self.node1.guid], 5.0)


class TestNetworkSetNodeCostByGUID(TestNetworkFunctionsBase):
    def runTest(self):
        self.network.setNodeCostByGUID(self.node1.guid, 5)
        self.assertEqual(self.network.node_costs[self.node1.guid], 5)


class TestNetworkSetNodeCostByName(TestNetworkFunctionsBase):
    def runTest(self):
        self.network.setNodeCostByName(self.node1.name, 5)
        self.assertEqual(self.network.node_costs[self.node1.guid], 5)


class TestNetworkSetEdgeCost(TestNetworkFunctionsBase):
    def runTest(self):
        self.network.setEdgeCost(self.edge, 5)
        self.assertEqual(self.network.edge_costs[self.edge.guid], 5)


class TestNetworkSetEdgeCostByGUID(TestNetworkFunctionsBase):
    def runTest(self):
        self.network.setEdgeCostByGUID(self.edge.guid, 5)
        self.assertEqual(self.network.edge_costs[self.edge.guid], 5)


class TestNetworkSetEdgeCostByName(TestNetworkFunctionsBase):
    def runTest(self):
        self.network.setEdgeCostByName(self.edge.name, 5)
        self.assertEqual(self.network.edge_costs[self.edge.guid], 5)


class TestNetworkGetNodeCost(TestNetworkFunctionsBase):
    def runTest(self):
        self.network.setNodeCost(self.node1, 5)  # tested above
        self.assertEqual(self.network.getNodeCost(self.node1),
                         self.network.node_costs[self.node1.guid])


class TestNetworkGetNodeCostByGUID(TestNetworkFunctionsBase):
    def runTest(self):
        self.network.setNodeCost(self.node1, 5)  # tested above
        self.assertEqual(self.network.getNodeCostByGUID(
            self.node1.guid), self.network.node_costs[self.node1.guid])


class TestNetworkGetNodeCostByName(TestNetworkFunctionsBase):
    def runTest(self):
        self.network.setNodeCost(self.node1, 5)  # tested above
        self.assertEqual(self.network.getNodeCostByName(
            self.node1.name), self.network.node_costs[self.node1.guid])


class TestNetworkGetEdgeCost(TestNetworkFunctionsBase):
    def runTest(self):
        self.network.setEdgeCost(self.edge, 5)  # tested above
        self.assertEqual(self.network.getEdgeCost(self.edge),
                         self.network.edge_costs[self.edge.guid])


class TestNetworkGetEdgeCostByGUID(TestNetworkFunctionsBase):
    def runTest(self):
        self.network.setEdgeCost(self.edge, 5)  # tested above
        self.assertEqual(self.network.getEdgeCostByGUID(
            self.edge.guid), self.network.edge_costs[self.edge.guid])


class TestNetworkGetEdgeCostByName(TestNetworkFunctionsBase):
    def runTest(self):
        self.network.setEdgeCost(self.edge, 5)  # tested above
        self.assertEqual(self.network.getEdgeCostByName(
            self.edge.name), self.network.edge_costs[self.edge.guid])


class TestNetworkReset(TestNetworkFunctionsBase):
    def runTest(self):
        self.network.reset()
        # check that all costs are equal to the node/edge's default cost
        for node in self.network.getNodes():
            self.assertEqual(self.network.node_costs[node.guid], node.cost)
        for edge in self.network.getEdges():
            self.assertEqual(self.network.edge_costs[edge.guid], edge.cost)


class TestNetworkUpdateCost(TestNetworkFunctionsBase):
    def runTest(self):
        self.network.updateCost(self.node1.guid, 5.0)
        self.assertEqual(self.network.node_costs[self.node1.guid], 5)


class TestNetworkUpdateCosts(TestNetworkFunctionsBase):
    def runTest(self):
        self.network.updateCosts({self.node1.guid: 5.0, self.node2.guid: 10.0})
        self.assertEqual(self.network.node_costs[self.node1.guid], 5)
        self.assertEqual(self.network.node_costs[self.node2.guid], 10)


class TestNetworkGetInteractionCosts(TestNetworkFunctionsBase):
    def runTest(self):
        # create a travel path from node1 to node2
        travel_path = [[self.node1, self.node2]]
        # get the interaction costs
        interaction_costs = self.network.getInteractionCosts(travel_path)
        # print the interaction costs
        print(interaction_costs)
        self.assertDictEqual(interaction_costs, {
            self.node1.guid: self.node1.cost,
            self.edge.guid: self.edge.cost,
            self.node2.guid: self.node2.cost
        })


class TestNetworkGetCompleteSystemCost(TestNetworkFunctionsBase):
    def runTest(self):
        # create a travel path from node1 to node2
        travel_path = [[self.node1, self.node2]]
        # get the interaction costs
        interaction_costs = self.network.getInteractionCosts(travel_path)
        # get the complete system cost
        complete_system_cost = self.network.getCompleteSystemCost()
        # print the complete system cost
        print(complete_system_cost)
        self.assertEqual(complete_system_cost, (self.node1.cost +
                         self.edge.cost + self.node2.cost)/3)


class TestNetworkGetSystemCost(TestNetworkFunctionsBase):
    def runTest(self):
        # create a travel path from node1 to node2
        travel_path = [[self.node1, self.node2]]
        system_cost = self.network.getSystemCost()
        # print the system cost
        print(system_cost)
        self.assertDictEqual(
            system_cost, {'testNode1': 0.3333333333333333, 'testNode2': 0.3333333333333333})


class TestNetworkGetNodeSystemCost(TestNetworkFunctionsBase):
    def runTest(self):
        # create a travel path from node1 to node2
        travel_path = [[self.node1, self.node2]]
        node_system_cost = self.network.getNodeSystemCost(
            self.node1)
        # print the node system cost
        print(node_system_cost)
        self.assertEqual(node_system_cost, 0.3333333333333333)

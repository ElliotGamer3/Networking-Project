# a test runner for the network class' unit tests
import unittest
from src.network.network import Network
from src.graph.node.node import Node
from src.graph.edge.edge import Edge
from tests.network.network.network_test import *


class TestNetworkRunner(unittest.TextTestRunner):
    # add the network's test suites to the test runner
    def __init__(self):
        super().__init__()
        # add the test suites to the test runner
        self.addTest(TestSetNodeCost())
        self.addTest(TestSetNodeCostByGUID())
        self.addTest(TestSetNodeCostByName())
        self.addTest(TestSetEdgeCost())
        self.addTest(TestSetEdgeCostByGUID())
        self.addTest(TestSetEdgeCostByName())
        self.addTest(TestGetNodeCost())
        self.addTest(TestGetNodeCostByGUID())
        self.addTest(TestGetNodeCostByName())
        self.addTest(TestGetEdgeCost())
        self.addTest(TestGetEdgeCostByGUID())
        self.addTest(TestGetEdgeCostByName())
        self.addTest(TestReset())
        


    def run(self):
        super().run()


if __name__ == "__main__":
    TestNetworkRunner().run()

# the test runner for the graph class' unit tests

import unittest
from src.graph.graph import Graph
from src.graph.node.node import Node
from src.graph.edge.edge import Edge
from src.graph.edge.directedEdge import DirectedEdge
from src.graph.edge.undirectedEdge import UndirectedEdge

from tests.graph.graph.graph_node_test import TestNodeFunctions

# test runner for the graph class' unit tests


class TestGraphRunner(unittest.TextTestRunner):
    # add the graph's test suites to the test runner
    def __init__(self):
        super().__init__()
        # add the test suites to the test runner
        self.addTest(TestNodeFunctions())

    # run the tests
    def run(self):
        super().run()


if __name__ == "__main__":
    TestGraphRunner().run()

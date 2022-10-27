#the test runner for the graph class' unit tests

import unittest
from graph.graph import Graph
from graph.node.node import Node
from graph.edge.edge import Edge
from graph.edge.directedEdge import DirectedEdge
from graph.edge.undirectedEdge import UndirectedEdge

from tests.graph.graph.graph_node_test import TestNodeFunctions

#test runner for the graph class' unit tests
class TestGraphRunner(unittest.TextTestRunner):
    #add the graph's test suites to the test runner
    def __init__(self):
        super().__init__()
        #add the test suites to the test runner
        self.addTest(TestNodeFunctions())
        pass
    #run the tests
    def run(self):
        super().run()
        pass

if __name__ == "__main__":
    TestGraphRunner().run()


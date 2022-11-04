# the test runner for the node class' unit tests
import unittest
from tests.graph.node.node.node_test import TestNodeFunctions


class TestNodeRunner(unittest.TextTestRunner):
    # add the node's test suites to the test runner
    def __init__(self):
        super().__init__()
        # add the test suites to the test runner
        self.addTest(TestNodeFunctions())

    def run(self):
        super().run()


if __name__ == "__main__":
    TestNodeRunner().run()

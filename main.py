import src.graph.graph as Graph
import src.graph.edge.edge as Edge
import src.graph.node.node as Node
from src.simulation.scenarios.simple_network import EveryNodeTravelerScenario

from sys import setrecursionlimit as sysRL
sysRL(10000)


def main():

    # create some nodes
    node1 = Node.Node("node1")
    node2 = Node.Node("node2")
    node3 = Node.Node("node3")
    # create some edges
    edge1 = Edge.Edge(node1, node2, 1, "edge1")
    edge2 = Edge.Edge(node2, node3, 1, "edge2")
    edge3 = Edge.Edge(node3, node1, 1, "edge3")
    # add the edges to a list
    edges = [edge1, edge2, edge3]
    # add the nodes to a list
    nodes = [node1, node2, node3]
    # create a graph with the nodes connected by the edges
    graph1 = Graph.Graph(edges)
    # create a graph with the nodes and no edges
    graph2 = Graph.Graph(nodes)
    # create a graph with no nodes and no edges
    graph3 = Graph.Graph([])
    print(graph1)
    print(graph2)
    print(graph3)
    print("finished basic graph tests")
    print("")

    # create a scenario
    scenario = EveryNodeTravelerScenario()
    scenario.run()
    print(scenario.network.graph)
    print(scenario.getLogs())

    return 0


if __name__ == "__main__":
    main()

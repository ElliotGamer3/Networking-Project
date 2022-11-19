import src.graph.graph as Graph
import src.graph.edge.edge as Edge
import src.graph.node.node as Node
from src.network.presets.network1 import Network1
from src.simulation.scenarios.simple_network import EveryNodeTravelerScenario
from src.simulation.scenarios.travelerScenario import TravelerScenario

from sys import setrecursionlimit as sysRL
sysRL(10000)


def main():

    # create some nodes
    node1 = Node.Node("node1", 0.0)
    node2 = Node.Node("node2", 0.0)
    node3 = Node.Node("node3", 0.0)
    # create some edges
    edge1 = Edge.Edge(node1, node2, 0, "edge1")
    edge2 = Edge.Edge(node2, node3, 0, "edge2")
    edge3 = Edge.Edge(node3, node1, 0, "edge3")
    # add the edges to a list
    edges = [edge1, edge2, edge3]
    # add the nodes to a list
    nodes = [node1, node2, node3]
    # create a graph with the nodes connected by the edges
    graph1 = Graph.Graph(edges)
    # create a graph with the nodes and no edges
    graph2 = Graph.Graph(nodes)
    # create a graph with no nodes and no edges
    graph3 = Graph.Graph(nodes+edges)
    print(graph1)
    print(graph2)
    print(graph3)
    print("finished basic graph tests")

    # create a scenario for basic goes to every node traveler
    scenario = EveryNodeTravelerScenario()
    scenario.run()
    print(scenario.network.graph)
    print(scenario.getLogs())

    # create a new scenario for a travelers

    scenario2 = TravelerScenario(Network1())
    scenario2.run()
    print(scenario2.network.graph)
    print(scenario2.getLogs())

    return 0


if __name__ == "__main__":
    main()

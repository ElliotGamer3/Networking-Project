from src.graph.node.node import Node
from src.graph.edge.edge import Edge
from src.graph.graph import Graph
from src.network.network import Network


class Network2:
    def __init__(self) -> None:
        # create some nodes
        node1 = Node("node1", 0.0)
        node2 = Node("node2", 0.0)
        node3 = Node("node3", 0.0)
        # create some edges
        edge1 = Edge(node1, node2, 0, "edge1")
        edge2 = Edge(node2, node3, 0, "edge2")
        edge3 = Edge(node3, node1, 0, "edge3")
        # add the edges to a list
        edges = [edge1, edge2, edge3]
        # add the nodes to a list
        nodes = [node1, node2, node3]

        # create the traveler paths
        traveler1 = [node1, node2, node3]
        traveler2 = [node1, node2, node3]
        traveler3 = [node1, node2, node3]
        traveler4 = [node1, node2, node1]
        traveler5 = [node3, node2, node1]
        traveler6 = [node3, node2, node1]
        traveler7 = [node3, node2, node1]

        # create the list of traveler paths
        travelers = [traveler1, traveler2, traveler3,
                     traveler4, traveler5, traveler6, traveler7]

        # create a network with the nodes connected by the edges
        self.network = Network(nodes+edges)
        self.travelers = travelers

from src.graph.node.node import Node
from src.graph.edge.edge import Edge
from src.graph.graph import Graph
from src.network.network import Network


class Network3:
    def __init__(self) -> None:
        # create some nodes
        node1 = Node("node1", 0.0)
        node2 = Node("node2", 0.0)
        node3 = Node("node3", 0.0)
        node4 = Node("node4", 0.0)
        node5 = Node("node5", 0.0)
        node6 = Node("node6", 0.0)
        node7 = Node("node7", 0.0)
        node8 = Node("node8", 0.0)
        node9 = Node("node9", 0.0)
        node10 = Node("node10", 0.0)
        node11 = Node("node11", 0.0)
        node12 = Node("node12", 0.0)
        node13 = Node("node13", 0.0)
        node14 = Node("node14", 0.0)
        node15 = Node("node15", 0.0)
        node16 = Node("node16", 0.0)
        node17 = Node("node17", 0.0)
        node18 = Node("node18", 0.0)
        node19 = Node("node19", 0.0)
        node20 = Node("node20", 0.0)
        # create some edges
        edge1 = Edge(node1, node2, 0, "edge1")
        edge2 = Edge(node2, node3, 0, "edge2")
        edge3 = Edge(node3, node1, 0, "edge3")
        edge4 = Edge(node4, node5, 0, "edge4")
        edge5 = Edge(node5, node6, 0, "edge5")
        edge6 = Edge(node6, node4, 0, "edge6")
        edge7 = Edge(node7, node8, 0, "edge7")
        edge8 = Edge(node8, node9, 0, "edge8")
        edge9 = Edge(node9, node7, 0, "edge9")
        edge10 = Edge(node10, node11, 0, "edge10")
        edge11 = Edge(node11, node12, 0, "edge11")
        edge12 = Edge(node12, node10, 0, "edge12")
        edge13 = Edge(node13, node14, 0, "edge13")
        edge14 = Edge(node14, node15, 0, "edge14")
        edge15 = Edge(node15, node13, 0, "edge15")
        edge16 = Edge(node16, node17, 0, "edge16")
        edge17 = Edge(node17, node18, 0, "edge17")
        edge18 = Edge(node18, node16, 0, "edge18")
        edge19 = Edge(node19, node20, 0, "edge19")
        edge20 = Edge(node20, node19, 0, "edge20")
        edge21 = Edge(node1, node4, 0, "edge21")
        edge22 = Edge(node4, node7, 0, "edge22")
        edge23 = Edge(node7, node10, 0, "edge23")
        edge24 = Edge(node10, node13, 0, "edge24")
        edge25 = Edge(node13, node16, 0, "edge25")
        edge26 = Edge(node16, node19, 0, "edge26")
        edge27 = Edge(node19, node1, 0, "edge27")
        edge28 = Edge(node2, node5, 0, "edge28")
        edge29 = Edge(node5, node8, 0, "edge29")
        edge30 = Edge(node8, node11, 0, "edge30")

        # add the nodes to the nodes list
        nodes = [node1, node2, node3, node4, node5, node6, node7, node8, node9, node10,
                 node11, node12, node13, node14, node15, node16, node17, node18, node19, node20]
        # add the edges to the edges list
        edges = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12, edge13, edge14, edge15,
                 edge16, edge17, edge18, edge19, edge20, edge21, edge22, edge23, edge24, edge25, edge26, edge27, edge28, edge29, edge30]

        # create traveler paths that visit at least 3 nodes and at most 10 nodes
        traveler1 = [node1, node4, node7, node10,
                     node13, node16, node19, node1]
        traveler2 = [node1, node4, node7, node10,
                     node13, node16, node19]
        traveler3 = [node1, node4, node7, node10,
                     node13, node16, node19]
        traveler4 = [node1, node4, node7, node10,
                     node13, node16, node19]
        traveler5 = [node1, node4, node7, node10,
                     node13, node16, node19]
        traveler6 = [node1, node4, node7, node10,
                     node13, node16, node19]
        traveler7 = [node1, node4, node7, node10,
                     node13, node16, node19]
        traveler8 = [node1, node4, node7, node10,
                     node13, node16, node19]
        traveler9 = [node1, node4, node7, node10,
                     node13, node16, node19]
        traveler10 = [node1, node4, node7,
                      node10, node13, node16, node19]
        traveler11 = [node1, node4, node7,
                      node10, node13, node16, node19]
        traveler12 = [node1, node4, node7,
                      node10, node13, node16, node19]
        traveler13 = [node1, node4, node7,
                      node10, node13, node16, node19]
        traveler14 = [node1, node4, node7,
                      node10, node13, node16, node19]
        traveler15 = [node1, node4, node7,
                      node10, node13, node16, node19]
        traveler16 = [node1, node4, node7,
                      node10, node13, node16, node19]
        traveler17 = [node1, node4, node7,
                      node10, node13, node16, node19]
        traveler18 = [node1, node4, node7,
                      node10, node13, node16, node19]
        traveler19 = [node1, node4, node7, node10, node13,
                      node16, node13, node10, node7, node4, node1]

        # create the list of traveler paths
        travelers = [traveler1, traveler2, traveler3, traveler4, traveler5, traveler6, traveler7, traveler8, traveler9,
                     traveler10, traveler11, traveler12, traveler13, traveler14, traveler15, traveler16, traveler17, traveler18]

        # create a network with the nodes connected by the edges
        self.network = Network(nodes+edges)
        self.travelers = travelers

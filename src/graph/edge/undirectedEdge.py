from src.graph.edge.edge import Edge
from src.graph.node.node import Node #import the edge class
class UndirectedEdge(Edge):
    def __init__(self, node1:Node, node2:Node, name:str=None) -> None:
        super().__init__(node1, node2, 0, name) #call the super constructor with direction 0
        pass

    
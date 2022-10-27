from src.graph.edge.edge import Edge as Edge
from src.graph.node.node import Node
#class for directed edge in a graph
class DirectedEdge(Edge):
    def __init__(self, node1 : Node, node2: Node, direction : int=None, name : str=None) -> None:
        super().__init__(node1, node2, direction, name) #call the super constructor with the direction defaulting to 1
        pass

from graph.graphable.graphable import Graphable
from graph.node.node import Node

#class to represent an edge in a graph
class Edge(Graphable):
    def __init__(self, node1:Node, node2:Node, direction:int=None, name:str=None) -> None:
        super().__init__(name=name) #call the super constructor with the name
        self.node1 = node1
        self.node2 = node2
        self._direction = direction #-1 = <--, 0 = ---, 1 = -->
        pass

    @property
    def direction(self) -> int:
        if self._direction == None:
            self._direction = 0
        return self._direction

    #return a string representation of the edge
    def __str__(self) -> str:
        if self._direction == 0:
            return f"{self.name}:{self.node1}---{self.node2}"
        elif self._direction == 1:
            return f"{self.name}:{self.node1}-->{self.node2}"
        elif self._direction == -1:
            return f"{self.name}:{self.node1}<--{self.node2}"
        else:
            raise Exception("Invalid direction")
    
    #compare two edges by the nodes they connect and direction node1->node2
    def __eq__(self, __o: object) -> bool:
        #if the direction is 0 then the edge is undirected so we need to check both directions
        if self._direction == 0:
            return (self.node1 == __o.node1 and self.node2 == __o.node2) or (self.node1 == __o.node2 and self.node2 == __o.node1)
        else: #otherwise just check the if the nodes are the same and the direction is the same
            return self.node1 == __o.node1 and self.node2 == __o.node2 and self._direction == __o.direction

    #the string that is used when the object is printed
    def __repr__(self) -> str:
        return self.__str__()
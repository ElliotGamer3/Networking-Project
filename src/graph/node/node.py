#class for a node in the graph
from graph.graphable.graphable import Graphable
class Node(Graphable):
    def __init__(self, name : str=None) -> None:
        super().__init__(name=name) #call the super constructor with the name as the type is set in the by the first get of the type property
        pass

    # override the getJSON method in the child class
    def getJSON(self) -> dict:
        return {
            "guid": self.guid,
            "type": self.type,
            "name": self.name
        }

    def __str__(self) -> str:
        return super().__str__()

    def __repr__(self) -> str:
        return super().__repr__()
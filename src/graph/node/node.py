from src.graph.graphable.graphable import Graphable
# class for a node in the graph


class Node(Graphable):
    def __init__(self, name: str = None, cost: float = None) -> None:
        # call the super constructor with the name and cost type is set by the property in the super class
        super().__init__(name=name, cost=cost)
        pass
    # override the getJSON method in the child class

    def getJSON(self) -> dict:
        return {
            "guid": self.guid,
            "type": self.type,
            "name": self.name,
            "cost": self.cost
        }

    def __str__(self) -> str:
        return super().__str__()

    def __repr__(self) -> str:
        return super().__repr__()

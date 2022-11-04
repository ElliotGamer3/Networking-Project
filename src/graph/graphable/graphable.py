# abstract class for all graphable objects
from uuid import uuid4
from src.utilities.guid import GUID


class Graphable:

    def __init__(self, type: str = None, guid: str = None, name: str = None, cost: float = None) -> None:
        self._type = type
        self._guid = guid
        self._name = name
        self._cost = cost
        pass

    # override the getJSON method in the child class
    def getJson(self) -> dict:
        raise NotImplementedError(
            f"Method getJson not implemented in {self.__class__.__name__}")

    @property
    def name(self) -> str:
        if self._name is None:
            self._name = f"{self.__class__.__name__} {self.guid}"
        return self._name

    @property
    def guid(self) -> str:
        if self._guid is None:  # if the guid is not set, set it to a new guid
            self._guid = uuid4().__str__()
        return self._guid  # return the guid

    @property
    def type(self) -> str:
        if self._type is None:  # if the type is not set, set it to the class name
            self._type = self.__class__.__name__  # get the name of the class
        return self._type  # return the type

    @property
    def cost(self) -> float:
        if self._cost is None:
            self._cost = 0.0
        return self._cost

    def __str__(self) -> str:
        return f"[{self.type}: {self.name} - ({self.guid})]"

    def __repr__(self) -> str:
        return self.__str__()

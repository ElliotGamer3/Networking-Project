#class that gives out GUIDs
from uuid import uuid4

class GUID:
    def __init__(self) -> None:
        self._guid = None

    def __call__(self) -> str:
        return str(self._guid)

    def __str__(self) -> str:
        return f"GUID: {self.guid}"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other) -> bool:
        return self.guid == other.guid

    def __ne__(self, other) -> bool:
        return self.guid != other.guid

    def __hash__(self) -> int:
        return hash(self.guid)

   #for getting the guid
    def guid(self) -> str:
        if self._guid is None:
            self._guid = self._generateGuid()
        return self._guid

    #generate a new guid
    def _generateGuid(self) -> str:
        return str(uuid4().__str__())


    
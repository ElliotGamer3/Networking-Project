#class that gives out GUIDs
import uuid

class GUID:
    def __init__(self) -> None:
        self._guid = None

    def __call__(self) -> str:
        return self.guid

    def __str__(self) -> str:
        return self.guid

    def __repr__(self) -> str:
        return self.guid

    def __eq__(self, other) -> bool:
        return self.guid == other.guid

    def __ne__(self, other) -> bool:
        return self.guid != other.guid

    def __hash__(self) -> int:
        return hash(self.guid)

    @property
    def guid(self) -> str:
        if self._guid is None:
            self._guid = uuid.uuid4().hex
        return self._guid

    
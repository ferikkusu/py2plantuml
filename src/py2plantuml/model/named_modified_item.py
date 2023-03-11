from abc import ABC, abstractmethod
from pydantic import BaseModel

from py2plantuml.model import AccessModifiers

class NamedModifiedItem(BaseModel, ABC):
    access_modifier: AccessModifiers
    name: str

    @abstractmethod
    def to_string(self) -> str:
        pass

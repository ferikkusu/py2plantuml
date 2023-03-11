from abc import ABC, abstractmethod
from typing import Any

from py2plantuml.model import AccessModifiers, NamedModifiedItem


class BaseParser(ABC):
    @abstractmethod
    def parse(self, data: Any) -> NamedModifiedItem:
        pass

    def get_access_modifier(self, line: str) -> AccessModifiers:
        if line.startswith("_"):
            return AccessModifiers.PRIVATE
        else:
            return AccessModifiers.PUBLIC

    def get_name(self, line: str) -> str:
        name: str = line.split(":")[0]
        if name.startswith("_"):
            return name[1:]
        else:
            return name

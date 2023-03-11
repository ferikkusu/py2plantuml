from typing import List

from py2plantuml.model import NamedModifiedItem, Field

class Class(NamedModifiedItem):
    fields: List[Field]

    def to_string(self) -> str:
        result: str = f"class {self.name}" + " {\n"
        for field in self.fields:
            result += f"    {field.to_string()}\n"
        result += "}"
        return result

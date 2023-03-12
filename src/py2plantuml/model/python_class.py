from pydantic import Field as PydanticField
from typing import List

from py2plantuml.model import NamedModifiedItem, Field, Function

class Class(NamedModifiedItem):
    parents: List["Class"] = PydanticField(default_factory=list)
    fields: List[Field]
    functions: List[Function]

    def to_string(self) -> str:
        result: str = f"class {self.name}" + " {\n"
        for field in self.fields:
            result += f"    {field.to_string()}\n"

        if len(self.functions) > 0:
            result += "\n"

        for function in self.functions:
            result += f"    {function.to_string()}\n"

        result += "}"

        if len(self.parents) > 0:
            for parent in self.parents:
                result += f"\n{parent.name} <|-- {self.name}"

        return result

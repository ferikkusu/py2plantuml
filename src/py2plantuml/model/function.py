from typing import List

from py2plantuml.model import AccessModifiers, NamedModifiedItem, FunctionArgument


class Function(NamedModifiedItem):
    arguments: List[FunctionArgument]
    return_type: str

    def to_string(self) -> str:
        modifier: str
        if self.access_modifier == AccessModifiers.PRIVATE:
            modifier = "-"
        else:
            modifier = "+"
        arguments_string: str = ", ".join([arg.to_string() for arg in self.arguments])
        return f"{modifier} {self.name}({arguments_string}): {self.return_type}"

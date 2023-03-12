from typing import List

from py2plantuml.model import FunctionArgument
from py2plantuml.parser import BaseParser


class FunctionArgumentParser(BaseParser):
    def parse(self, data: str) -> FunctionArgument:
        parts: List[str] = data.split(":")
        name: str = parts[0].strip()
        if name == "":
            raise ValueError(f"Could not parse FunctionArgument from line '{data}'")
        if len(parts) == 1:
            return FunctionArgument(
                name=name,
                type="Any"
            )
        elif len(parts) == 2:
            return FunctionArgument(
                name=name,
                type=parts[1].strip()
            )
        else:
            raise ValueError(f"Could not parse FunctionArgument from line '{data}'")

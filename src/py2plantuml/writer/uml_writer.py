from io import TextIOWrapper
from pydantic import BaseModel
from typing import List

from py2plantuml.model import Class


class UmlWriter(BaseModel):
    items: List[Class]

    def write(self, output_file: TextIOWrapper) -> None:
        output_file.write("@startuml\n")
        for item in self.items:
            output_file.write(item.to_string() + "\n")
        output_file.write("@enduml")

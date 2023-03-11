from typing import List

from py2plantuml.model import AccessModifiers, NamedModifiedItem
from py2plantuml.parser import BaseParser


class ClassParser(BaseParser):
    def parse(self, data: List[str]) -> NamedModifiedItem:
        class_definition_line: str = self._find_definition_line(lines=data)
        class_definition_line = class_definition_line[5:].strip()
        modifier: AccessModifiers = self.get_access_modifier(line=class_definition_line)
        name: str = self.get_name(line=class_definition_line)
        return NamedModifiedItem(
            access_modifier=modifier,
            name=name
        )

    def _find_definition_line(self, lines: List[str]) -> str:
        for line in lines:
            if line.strip().startswith("class"):
                return line.strip()
        raise ValueError("Could not find class definition line.")

    def get_name(self, line: str) -> str:
        name_line: str = line
        if "(" in line:
            inheritance_start_index: int = line.index("(")
            inheritance_stop_index: int = line.index(")")
            name_line = line[0:inheritance_start_index]
            name_line += line[inheritance_stop_index + 1:]
        return super().get_name(line=name_line)

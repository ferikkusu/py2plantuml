from py2plantuml.model import AccessModifiers, Field
from py2plantuml.parser import BaseParser


class FieldParser(BaseParser):
    def parse(self, data: str) -> Field:
        line: str = data.strip()
        modifier: AccessModifiers = self.get_access_modifier(line=line)
        name: str = self.get_name(line=line)
        field_type: str = self.get_type(line=line)
        return Field(
            access_modifier=modifier,
            name=name,
            type=field_type
        )

    def get_type(self, line: str) -> str:
        field_type: str = line.split(":")[1]
        return field_type.strip()

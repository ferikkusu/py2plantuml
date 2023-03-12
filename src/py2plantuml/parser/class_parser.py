from typing import List

from py2plantuml.model import AccessModifiers, Class, Field, Function
from py2plantuml.parser import BaseParser, FieldParser, FunctionParser


class ClassParser(BaseParser):
    def parse(self, data: List[str]) -> Class:
        class_definition_line: str = self._find_definition_line(lines=data)
        class_definition_line = class_definition_line[5:].strip()
        modifier: AccessModifiers = self.get_access_modifier(line=class_definition_line)
        name: str = self.get_name(line=class_definition_line)

        fields: List[Field] = self._parse_fields(data=data)
        functions: List[Function] = self._parse_functions(data=data)

        return Class(
            access_modifier=modifier,
            name=name,
            fields=fields,
            functions=functions
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

    def _parse_fields(self, data: List[str]) -> List[Field]:
        field_lines: List[str] = self._find_field_lines(lines=data)
        parser: FieldParser = FieldParser()
        fields: List[Field] = []

        for field_line in field_lines:
            if field_line.strip() != "":
                fields.append(parser.parse(data=field_line))

        return fields        

    def _find_field_lines(self, lines: List[str]) -> List[str]:
        class_definition_line_index: int = -1
        first_function_definition_line_index: int = -1
        for i in range(len(lines)):
            if lines[i].strip().startswith("class"):
                class_definition_line_index = i
            elif lines[i].strip().startswith("def"):
                first_function_definition_line_index = i
                break
        
        return lines[class_definition_line_index+1:first_function_definition_line_index]

    def _parse_functions(self, data: List[str]) -> List[Function]:
        functions: List[Function] = []
        function_parser: FunctionParser = FunctionParser()
        for function_line in self._find_function_lines(lines=data):
            functions.append(function_parser.parse(data=function_line))
        return functions

    def _find_function_lines(self, lines: List[str]) -> List[str]:
        function_lines: List[str] = [line.strip() for line in lines if line.strip().startswith("def ")]
        return function_lines

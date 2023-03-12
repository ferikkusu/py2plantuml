from loguru import logger
from typing import List

from py2plantuml.model import AccessModifiers, FunctionArgument, Function
from py2plantuml.parser import BaseParser, FunctionArgumentParser


class FunctionParser(BaseParser):
    def parse(self, data: str) -> Function:
        line: str = data.strip()
        if line.startswith("def"):
            line = line[4:]
        modifier: AccessModifiers = self.get_access_modifier(line=line)
        name: str = self.get_name(line=line)
        return_type: str = self.get_type(line=line)
        arguments: List[FunctionArgument] = self.get_arguments(line=line)

        return Function(
            access_modifier=modifier,
            name=name,
            return_type=return_type,
            arguments=arguments
        )

    def get_name(self, line: str) -> str:
        line_without_arguments: str = line[:line.index("(")]
        if "__init__" in line_without_arguments:
            return "__init__"
        return super().get_name(line=line_without_arguments)

    def get_type(self, line: str) -> str:
        try:
            field_type: str = line.split("->")[1]
            return field_type.replace(":", "").strip()
        except IndexError:
            return "Any"
        
    def get_arguments(self, line: str) -> List[FunctionArgument]:
        arguments_start_index: int = line.index("(")
        arguments_end_index: int = line.index(")")
        arguments_line: str = line[arguments_start_index+1:arguments_end_index]
        arguments_line = arguments_line.replace("self,", "").replace("self", "").strip()
        arguments: List[str] = arguments_line.split(",")

        argument_parser: FunctionArgumentParser = FunctionArgumentParser()
        function_arguments: List[FunctionArgument] = []
        for argument in arguments:
            try:
                function_arguments.append(argument_parser.parse(argument))
            except ValueError as e:
                logger.warning(e)
        return function_arguments

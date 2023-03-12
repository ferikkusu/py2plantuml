from unittest import TestCase
from unittest.mock import MagicMock, patch
from parameterized import parameterized

from typing import List

from py2plantuml.model import AccessModifiers, Function, FunctionArgument
from py2plantuml.parser import FunctionParser


class FunctionParserTest(TestCase):

    @parameterized.expand([
        ("   def function(argument_1: str) -> None:", "None"),
        ("   def function(argument_1: str):", "Any")
    ])
    def test_get_type_with_type_hint(self, line: str, expected: str) -> None:
        # given
        class_under_test: FunctionParser = FunctionParser()

        # when
        actual: str = class_under_test.get_type(line=line)

        # then
        assert actual == expected

    @parameterized.expand([
        ("  def function(self):", 0),
        ("def function(self, argument_1: int):", 1),
        ("def function(self, argument_1: int, argument_2: str):", 2)
    ])
    def test_get_arguments_different_amounts(self, line: str, expected: int) -> None:
        # given
        class_under_test: FunctionParser = FunctionParser()

        # when
        actual: int = len(class_under_test.get_arguments(line=line))

        # then
        assert actual == expected

    def test_get_arguments(self) -> None:
        # given
        line: str = "def function(self, argument_1: int, argument_2: str):"
        class_under_test: FunctionParser = FunctionParser()

        # when
        actual: List[FunctionArgument] = class_under_test.get_arguments(line=line)

        # then
        expected: List[FunctionArgument] = [
            FunctionArgument(
                name="argument_1",
                type="int"
            ),
            FunctionArgument(
                name="argument_2",
                type="str"
            )
        ]

        assert actual == expected

    def test_parse(self) -> None:
        # given
        get_type_mock: MagicMock = MagicMock(return_value="type")
        get_arguments_mock: MagicMock = MagicMock(return_value=[])

        line: str = " def function(self, argument_1: int) -> type:"
        class_under_test: FunctionParser = FunctionParser()

        # when
        with patch.multiple(FunctionParser, get_type=get_type_mock, get_arguments=get_arguments_mock):
            actual: Function = class_under_test.parse(data=line)

        # then
        expected: Function = Function(
            access_modifier=AccessModifiers.PUBLIC,
            arguments=get_arguments_mock.return_value,
            name="function",
            return_type=get_type_mock.return_value
        )

        assert actual == expected

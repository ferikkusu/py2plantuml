from unittest import TestCase

from py2plantuml.model import FunctionArgument
from py2plantuml.parser import FunctionArgumentParser


class FunctionArgumentParserTest(TestCase):
    def test_parse_with_invalid_string(self) -> None:
        # given
        test_string: str = "argument_1: str, argument_2: int"
        class_under_test: FunctionArgumentParser = FunctionArgumentParser()

        # when / then
        self.assertRaises(ValueError, class_under_test.parse, test_string)

    def test_parse_without_type_hint(self) -> None:
        # given
        test_string: str = " argument_1  "
        class_under_test: FunctionArgumentParser = FunctionArgumentParser()

        # when
        actual: FunctionArgument = class_under_test.parse(data=test_string)

        # then
        expected: FunctionArgument = FunctionArgument(name="argument_1", type="Any")

        assert actual == expected

    def test_parse_with_type_hint(self) -> None:
        # given
        test_string: str = " argument_1: str  "
        class_under_test: FunctionArgumentParser = FunctionArgumentParser()

        # when
        actual: FunctionArgument = class_under_test.parse(data=test_string)

        # then
        expected: FunctionArgument = FunctionArgument(name="argument_1", type="str")

        assert actual == expected

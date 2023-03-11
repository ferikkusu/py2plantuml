from unittest import TestCase

from typing import List

from py2plantuml.model import AccessModifiers, NamedModifiedItem
from py2plantuml.parser import ClassParser


class ClassParserTest(TestCase):
    def test_parse_should_throw_error(self) -> None:
        # given
        empty_test_data: List[str] = []
        class_under_test: ClassParser = ClassParser()

        # when / then
        self.assertRaises(ValueError, class_under_test.parse, empty_test_data)

    def test_parse_should_return_item(self) -> None:
        # given
        class_definition_line: str = "  class _TestClass(Parent): \n"
        class_under_test: ClassParser = ClassParser()

        # when
        actual: NamedModifiedItem = class_under_test.parse(data=[class_definition_line])

        # then
        expected: NamedModifiedItem = NamedModifiedItem(
            access_modifier=AccessModifiers.PRIVATE,
            name="TestClass"
        )
        
        assert actual == expected

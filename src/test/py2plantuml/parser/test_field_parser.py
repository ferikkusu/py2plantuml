from unittest import TestCase

from py2plantuml.model import AccessModifiers, Field
from py2plantuml.parser import FieldParser


class FieldParserTest(TestCase):
    def test_parse_should_return_public_field(self) -> None:
        # given
        test_line: str = "    public_integer_field: int"
        expected: Field = Field(
            access_modifier=AccessModifiers.PUBLIC,
            name="public_integer_field",
            type="int"
        )
        class_under_test: FieldParser = FieldParser()

        # when
        actual: Field = class_under_test.parse(data=test_line)

        # then
        assert actual == expected

    def test_parse_should_return_private_field(self) -> None:
        # given
        test_line: str = "    _private_integer_field: int"
        expected: Field = Field(
            access_modifier=AccessModifiers.PRIVATE,
            name="private_integer_field",
            type="int"
        )
        class_under_test: FieldParser = FieldParser()

        # when
        actual: Field = class_under_test.parse(data=test_line)

        # then
        assert actual == expected

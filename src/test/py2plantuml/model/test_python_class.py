from unittest import TestCase
from unittest.mock import MagicMock, patch

from py2plantuml.model import AccessModifiers, Class, Field


class ClassTest(TestCase):
    def test_to_string(self) -> None:
        # given
        field: Field = Field(
            access_modifier=AccessModifiers.PUBLIC,
            name="testField",
            type="str"
        )
        class_under_test: Class = Class(
            access_modifier=AccessModifiers.PUBLIC,
            name="TestClass",
            fields=[field]
        )
        field_to_string_mock: MagicMock = MagicMock(return_value="FieldString")

        # when
        with patch.object(Field, "to_string", field_to_string_mock):
            actual: str = class_under_test.to_string()

        # then
        expected: str = "class TestClass {\n    FieldString\n}"

        assert actual == expected
        assert field_to_string_mock.call_count == len(class_under_test.fields)

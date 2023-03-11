from unittest import TestCase
from parameterized import parameterized

from py2plantuml.model import AccessModifiers, Field


class FieldTest(TestCase):
    @parameterized.expand([
        (AccessModifiers.PRIVATE, "-"),
        (AccessModifiers.PUBLIC, "+")
    ])
    def test_to_string(self, modifier: AccessModifiers, modifier_string: str) -> None:
        # given
        class_under_test: Field = Field(
            access_modifier=modifier,
            name="FieldName",
            type="str"
        )

        # when
        actual: str = class_under_test.to_string()

        # then
        expected: str = f"{modifier_string} FieldName: str"
        
        assert actual == expected

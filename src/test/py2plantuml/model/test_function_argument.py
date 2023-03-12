from unittest import TestCase
from parameterized import parameterized

from py2plantuml.model import AccessModifiers, FunctionArgument


class FunctionArgumentTest(TestCase):
    def test_to_string_with_modifiers(self) -> None:
        # given
        class_under_test: FunctionArgument = FunctionArgument(
            access_modifier=AccessModifiers.PRIVATE,
            name="ArgumentName",
            type="str"
        )

        # when
        actual: str = class_under_test.to_string()

        # then
        expected: str = f"ArgumentName: str"
        
        assert actual == expected

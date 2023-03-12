from unittest import TestCase
from parameterized import parameterized

from py2plantuml.model import AccessModifiers, FunctionArgument, Function


class FunctionTest(TestCase):
    @parameterized.expand([
        (AccessModifiers.PRIVATE, "-"),
        (AccessModifiers.PUBLIC, "+")
    ])
    def test_to_string_with_modifiers(self, modifier: AccessModifiers, modifier_string: str) -> None:
        # given
        class_under_test: Function = Function(
            access_modifier=modifier,
            name="FunctionName",
            arguments=[],
            return_type="str"
        )

        # when
        actual: str = class_under_test.to_string()

        # then
        expected: str = f"{modifier_string} FunctionName(): str"
        
        assert actual == expected

    def test_to_string_with_one_arguments(self) -> None:
        # given
        class_under_test: Function = Function(
            access_modifier=AccessModifiers.PUBLIC,
            name="FunctionName",
            arguments=[
                FunctionArgument(
                    name="argument_1",
                    type="int"
                )
            ],
            return_type="str"
        )

        # when
        actual: str = class_under_test.to_string()

        # then
        expected: str = f"+ FunctionName(argument_1: int): str"

        assert actual == expected

    def test_to_string_with_two_arguments(self) -> None:
        # given
        class_under_test: Function = Function(
            access_modifier=AccessModifiers.PUBLIC,
            name="FunctionName",
            arguments=[
                FunctionArgument(
                    name="argument_1",
                    type="int"
                ),
                FunctionArgument(
                    name="argument_2",
                    type="str"
                )
            ],
            return_type="str"
        )

        # when
        actual: str = class_under_test.to_string()

        # then
        expected: str = f"+ FunctionName(argument_1: int, argument_2: str): str"

        assert actual == expected
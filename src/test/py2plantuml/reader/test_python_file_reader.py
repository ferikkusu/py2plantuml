from unittest import TestCase
from unittest.mock import MagicMock, patch
from parameterized import parameterized

import os

from typing import List

from py2plantuml.reader import PythonFileReader


class PythonFileReaderTest(TestCase):

    @parameterized.expand([
        ([["1", "2"], ["3", "4"]], True),
        ([], False)
    ])
    def test_contains_class_definition(self, class_lines: List[List[str]], expected: bool) -> None:
        # given
        test_class_path: str = os.path.join("src", "test", "test_data", "test_class.py")
        find_classes_mock: MagicMock = MagicMock(return_value=class_lines)
        class_under_test: PythonFileReader = PythonFileReader(python_file_path=test_class_path)

        # when
        with patch.object(PythonFileReader, "find_classes", find_classes_mock):
            actual: bool = class_under_test.contains_class_definition()

        # then
        assert actual == expected

    @parameterized.expand([
        ("FirstLevelClass", True),
        ("NotExistingClass", False)
    ])
    def test_contains_specified_class_definition(self, class_name: str, expected: bool) -> None:
        # given
        test_class_path: str = os.path.join("src", "test", "test_data", "test_class.py")
        class_under_test: PythonFileReader = PythonFileReader(python_file_path=test_class_path)

        # when
        actual: bool = class_under_test.contains_specified_class_definition(class_name=class_name)

        # then
        assert actual == expected

    def test_find_classes(self) -> None:
        # given
        test_class_path: str = os.path.join("src", "test", "test_data", "test_class.py")
        class_under_test: PythonFileReader = PythonFileReader(python_file_path=test_class_path)

        # when
        actual: List[List[str]] = class_under_test.find_classes()

        # then
        len(actual) == 1
        len(actual[0]) > 0

from unittest import TestCase
from unittest.mock import create_autospec, MagicMock, patch
from tempfile import TemporaryDirectory

import os

from typing import List

from py2plantuml.model import Class
from py2plantuml.writer import UmlWriter


class UmlWriterTest(TestCase):
    temp_dir: TemporaryDirectory

    def setUp(self) -> None:
        self.temp_dir = TemporaryDirectory()

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_write(self) -> None:
        # given
        item_mock: Class = create_autospec(Class)
        class_under_test: UmlWriter = UmlWriter(items=[item_mock])
        class_under_test.items[0].to_string = MagicMock(return_value="test_item_content")

        test_output_file = open(os.path.join(self.temp_dir.name, "test.txt"), "w")

        # when
        class_under_test.write(output_file=test_output_file)
        test_output_file.close()
        with open(os.path.join(self.temp_dir.name, "test.txt"), "r") as output:
            actual: List[str] = output.readlines()

        # then
        assert actual[0] == "@startuml\n"
        assert actual[1] == "test_item_content\n"
        assert actual[2] == "@enduml"

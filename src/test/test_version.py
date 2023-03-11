from unittest import TestCase

import re

from py2plantuml._version import get_version

class VersionTest(TestCase):
    def test_get_version(self) -> None:
        # given
        match_pattern: str = "\d*\.\d*\.\d*"

        # when
        actual = re.match(match_pattern, get_version())

        # then
        assert actual != None

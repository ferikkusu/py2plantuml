from typing import List

from py2plantuml.model import NamedModifiedItem, Field

class Class(NamedModifiedItem):
    fields: List[Field]

from pydantic import BaseModel

from py2plantuml.model import AccessModifiers

class NamedModifiedItem(BaseModel):
    access_modifier: AccessModifiers
    name: str

from py2plantuml.model import AccessModifiers, NamedModifiedItem


class FunctionArgument(NamedModifiedItem):
    access_modifier: AccessModifiers = AccessModifiers.PUBLIC
    type: str

    def to_string(self) -> str:
        return f"{self.name}: {self.type}"

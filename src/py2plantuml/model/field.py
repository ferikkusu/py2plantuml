from py2plantuml.model import AccessModifiers, NamedModifiedItem

class Field(NamedModifiedItem):
    type: str

    def to_string(self) -> str:
        modifier: str
        if self.access_modifier == AccessModifiers.PRIVATE:
            modifier = "-"
        else:
            modifier = "+"
        return f"{modifier} {self.name}: {self.type}"

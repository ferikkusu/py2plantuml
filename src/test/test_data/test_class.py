from pydantic import BaseModel


class FirstLevelClass(BaseModel):
    public_integer_field: int
    _private_string_field: str

    def __init__(self) -> None:
        self.public_integer_field = 0
        self._private_string_field = "string"

    def public_non_abstract_function(self, first_arguent: int, second_argument: str) -> str:
        return f"{first_arguent}_{second_argument}"

    def _private_non_abstract_function(self, first_argument: str, second_argument: int) -> str:
        return f"{first_argument}_{second_argument}"

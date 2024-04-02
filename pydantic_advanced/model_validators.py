from typing import Annotated

from pydantic import BaseModel, AfterValidator


def must_be_hex(value: str) -> str:
    assert


class User(BaseModel):
    id: int
    name: str
    email: Annotated[str, AfterValidator()]

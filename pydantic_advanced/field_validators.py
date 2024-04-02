from datetime import datetime
from typing import Annotated
from uuid import uuid4

from pydantic import BaseModel, AfterValidator


def must_be_positive(value: float) -> float:
    assert value > 0, 'value must be positive'
    return value


class Transaction(BaseModel):
    id: str
    timestamp: datetime
    amount: Annotated[float, AfterValidator(must_be_positive)]


Transaction(id=uuid4().hex, timestamp=datetime.now(), amount=-1.23)

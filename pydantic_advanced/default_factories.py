from datetime import datetime
from typing import Annotated
from uuid import uuid4

from pydantic import BaseModel, Field


def generate_id() -> str:
    return uuid4().hex

def generate_tim



class Transaction(BaseModel):
    id: Annotated[str, Field(default_factory=generate_id)]
    timestamp: Annotated[datetime, Field(default_factory=)]
    amount:

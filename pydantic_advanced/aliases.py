from datetime import datetime
from typing import Annotated
from uuid import uuid4

from pydantic import BaseModel, Field


class Transaction(BaseModel):
    id: Annotated[str, Field(validation_alias='transaction_id')]
    timestamp: Annotated[datetime, Field(serialization_alias='created_at')]
    amount: float


transaction = Transaction(**{'transaction_id': uuid4().hex, 'timestamp': datetime.now(), 'amount': 1.23})

transaction.model_dump(by_alias=True)

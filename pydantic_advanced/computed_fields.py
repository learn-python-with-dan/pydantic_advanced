from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, computed_field


class Transaction(BaseModel):
    id: str
    timestamp: datetime
    amount: float

    @computed_field
    def fee(self) -> float:
        return 0.01 + 0.01 * self.amount


transaction = Transaction(id=uuid4().hex, timestamp=datetime.now(), amount=1.23)

transaction.model_dump()

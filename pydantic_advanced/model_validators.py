from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, model_validator


class Transaction(BaseModel):
    id: str
    timestamp: datetime
    amount: float
    payer_id: int
    payee_id: int

    @model_validator(mode='after')
    def must_be_different(self):
        assert self.payer_id != self.payee_id, 'Payer and payee cannot be the same'


Transaction(id=uuid4().hex, timestamp=datetime.now(), amount=1.23, payer_id=1, payee_id=1)

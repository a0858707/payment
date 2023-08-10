from datetime import datetime
from pydantic import BaseModel

# model for transfer card to card
class P2PDent(BaseModel):
    card_from: int
    amount: float
    card_to: int
    transfer_time: datetime

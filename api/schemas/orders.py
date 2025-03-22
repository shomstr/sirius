from __future__ import annotations

from pydantic import BaseModel

class Order(BaseModel):
    user_id: int

    order_amount: int
    address: str
    fuel_load: int
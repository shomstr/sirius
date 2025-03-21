from __future__ import annotations

from typing import Sequence
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from .base import BaseRepo
from api.database.models import CarWash


class СarWashRepo(BaseRepo):
    model = CarWash

    async def get_car(self, car_id: int):
        q = select(CarWash).where(CarWash.car_id == car_id)

        return (await self.session.execute(q)).scalar()





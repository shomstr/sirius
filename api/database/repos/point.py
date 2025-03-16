from __future__ import annotations

from datetime import datetime
from typing import Sequence
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import selectinload

from .base import BaseRepo
from ..models import Point, PointConnector, PointCoordinate, PointOpeningTime
from api.schemas import Point as PointSchema

class PointsRepo(BaseRepo):
    model = Point

    async def create(
            self,
            point: PointSchema
            ):
        point_id = int(point.id)

        p = Point(
            id=point_id,
            name=point.name,
            address=point.address,
            city=point.city,
            active=point.active,
        )
        p.coordinates = PointCoordinate(
            point_id=point_id,
            latitude=point.coordinates[0],
            longitude=point.coordinates[1]
        )
        p.opening_times = PointOpeningTime(
            point_id=point_id,
            always_open=point.opening_times.always_open,
            charging_when_closed=point.opening_times.charging_when_closed
        )
        p.connectors = [
            PointConnector(
                point_id=point_id,
                id=int(connector.id),
                name=connector.name,
                connector=connector.connector,
                power=connector.power,
                state=connector.state,
                changed_at=datetime.strptime(connector.changed_at, "%Y-%m-%dT%H:%M:%SZ"),
                active=connector.active
            ) for evs in point.evses for connector in evs.connectors
        ]


        self.session.add(p)
        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()

    async def get_all_points_coordinates(self) -> int | Sequence[PointCoordinate]:
        result = await self.session.execute(select(PointCoordinate))
        return result.scalars().all()











from __future__ import annotations

from datetime import datetime
from typing import Self, Sequence

from pydantic import EmailStr
from sqlalchemy import String, select, ForeignKey, func, sql, Text, Integer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, relationship, joinedload
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.mysql import VARCHAR, DATETIME
from .base_models import Base
from .types import str255, intpk


# {
#       "id": "2712",
#       "active": true,
#       "name": "GREEN DRIVE Бизнес-квартал «Арма»",
#       "description": "",
#       "coordinates": [
#         55.759574,
#         37.663316
#       ],
#       "address": "Нижний Сусальный пер, д. 5",
#       "city": "",
#       "contacts": [],
#       "opening_times": {
#         "always_open": true,
#         "open_hours": [],
#         "charging_when_closed": true,
#         "exceptional_openings": [],
#         "exceptional_closings": []
#       },
#       "photos": [],
#       "evses": [
#         {
#           "id": "12787",
#           "connectors": [
#             {
#               "id": "12787",
#               "name": "GB/T - 1",
#               "active": true,
#               "connector": "GB/T DC",
#               "power": 120,
#               "state": "unknown",
#               "changed_at": "2024-05-15T14:00:42Z"
#             }
#           ],
#           "state": "unknown",
#           "changed_at": "2024-05-15T14:00:42Z"
#         },
class Point(Base):
    __tablename__ = "points"

    id: Mapped[intpk]
    name: Mapped[str255]

    active: Mapped[bool] = mapped_column(server_default=sql.false())
    description: Mapped[str] = mapped_column(Text, server_default="")

    # address
    address: Mapped[str255]
    city: Mapped[str255]

    coordinates: Mapped["PointCoordinate"] = relationship(
        lazy="joined",
        foreign_keys="PointCoordinate.point_id",
        uselist=False,
        passive_deletes=True,
        cascade="all, delete",
        post_update=True
    )

    opening_times: Mapped["PointOpeningTime"] = relationship(
        lazy="joined",
        foreign_keys="PointOpeningTime.point_id",
        uselist=False,
        passive_deletes=True,
        cascade="all, delete",
        post_update=True,
    )

    connectors: Mapped[list["PointConnector"]] = relationship(
        lazy="selectin",
        foreign_keys="PointConnector.point_id",
        passive_deletes=True,
        cascade="all, delete",
        post_update=True,

    )

    @staticmethod
    async def create(
            db: AsyncSession,
            id: int,
            name: str,
            address: str,
            city: str,
            active: bool = False,
            ) -> "Point":

        point = Point(
            id=id,
            name = name,
            address = address,
            city = city,
            active = active,
        )
        db.add(point)
        await db.commit()

        return point

    @staticmethod
    async def get(
            db: AsyncSession,
            id: int
    ) -> Point | None:

        q = select(Point).where(Point.id == id)
        user = (await db.execute(q)).scalar()
        return user



class PointCoordinate(Base):
    __tablename__ = "points_coordinates"

    point_id: Mapped[int] = mapped_column(Integer, ForeignKey(Point.id, ondelete="CASCADE"), nullable=False, primary_key=True)

    latitude: Mapped[float]
    longitude: Mapped[float]

    @staticmethod
    async def create(
            db: AsyncSession,
            point_id: int,
            latitude: float,
            longitude: float,
    ) -> "PointCoordinate":
        coordinate = PointCoordinate(
            point_id=point_id,
            latitude=latitude,
            longitude=longitude
        )
        db.add(coordinate)
        await db.commit()

        return coordinate

class PointOpeningTime(Base):
    __tablename__ = "points_opening_times"

    point_id: Mapped[int] = mapped_column(Integer, ForeignKey(Point.id, ondelete="CASCADE"), nullable=False, primary_key=True)

    always_open: Mapped[bool] = mapped_column(server_default=sql.false())
    #open_hours = []
    charging_when_closed: Mapped[bool] = mapped_column(server_default=sql.false())
    #exceptional_openings = []
    #exceptional_closings = []

    @staticmethod
    async def create(
            db: AsyncSession,
            point_id: int,
            always_open: bool = False,
            charging_when_closed: bool = False,
    ) -> "PointOpeningTime":
        opening_time = PointOpeningTime(
            point_id=point_id,
            always_open=always_open,
            charging_when_closed=charging_when_closed
        )
        db.add(opening_time)
        await db.commit()

        return opening_time

class PointConnector(Base):
    __tablename__ = "points_connectors"

    id: Mapped[intpk]
    point_id: Mapped[int] = mapped_column(Integer, ForeignKey(Point.id, ondelete="CASCADE"), nullable=False)

    name: Mapped[str255]
    active: Mapped[bool] = mapped_column(server_default=sql.false())

    connector: Mapped[str255]
    power: Mapped[int]
    state: Mapped[str] = mapped_column(server_default="unknown")
    changed_at: Mapped[datetime] = mapped_column(onupdate=func.now())

    @staticmethod
    async def create(
            db: AsyncSession,
            point_id: int,
            id: int,
            name: str,
            connector: str,

            power: int,
            state: str = "unknown",
            changed_at: datetime = datetime.now(),
            active: bool = False
    ) -> "PointConnector":

        con = PointConnector(
            point_id = point_id,
            id = id,
            name = name,
            connector = connector,
            power = power,
            state = state,
            changed_at = changed_at,
            active = active
        )
        db.add(con)
        await db.commit()

        return con
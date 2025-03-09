from datetime import datetime
from typing import List, Optional

from sqlalchemy import String, ForeignKey, Boolean, JSON, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.asyncio import AsyncSession
from models.schemas import stations

from models import Base  # Убедитесь, что Base импортирован правильно

class Station(Base):
    __tablename__ = "stations"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    active: Mapped[bool] = mapped_column(Boolean)
    name: Mapped[str] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String)
    coordinates: Mapped[List[float]] = mapped_column(JSON)  # или две колонки: latitude и longitude
    address: Mapped[str] = mapped_column(String)
    city: Mapped[Optional[str]] = mapped_column(String)
    time_zone: Mapped[str] = mapped_column(String)
    changed_at: Mapped[str] = mapped_column(String)

    evses: Mapped[List["EVSE"]] = relationship("EVSE", back_populates="station")

    
class EVSE(Base):
    __tablename__ = "evses"
    id: Mapped[int] = mapped_column(autoincrement=True,  primary_key=True, index=True)
    station_id: Mapped[int] = mapped_column(String, ForeignKey("stations.id"))
    state: Mapped[str] = mapped_column(String)
    changed_at: Mapped[str] = mapped_column(String)

    station: Mapped["Station"] = relationship("Station", back_populates="evses")
    connectors: Mapped[List["Connector"]] = relationship("Connector", back_populates="evse")

class Connector(Base):
    __tablename__ = "connectors"

    evse_id: Mapped[str] = mapped_column(String, ForeignKey("evses.id"),primary_key=True, index=True)
    name: Mapped[Optional[str]] = mapped_column(String)
    active: Mapped[bool] = mapped_column(Boolean)
    connector: Mapped[str] = mapped_column(String)
    power: Mapped[int] = mapped_column(Integer)
    state: Mapped[str] = mapped_column(String)
    changed_at: Mapped[str] = mapped_column(String)

    evse: Mapped["EVSE"] = relationship("EVSE", back_populates="connectors")
from __future__ import annotations

from pydantic import BaseModel


class OpeningTimes(BaseModel):
    always_open: bool
    open_hours: list
    charging_when_closed: bool
    exceptional_openings: list
    exceptional_closings: list


class Connector(BaseModel):
    id: str
    name: str
    active: bool
    connector: str
    power: int
    state: str
    changed_at: str


class Evse(BaseModel):
    id: str
    connectors: list[Connector]
    state: str
    changed_at: str


class Point(BaseModel):
    id: str
    active: bool
    name: str
    description: str
    coordinates: list[float]
    address: str
    city: str
    contacts: list
    opening_times: OpeningTimes
    photos: list
    evses: list[Evse]


class PointModel(BaseModel):
    points: list[Point]

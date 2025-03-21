from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fastapi import APIRouter

from . import point, car_wash
routers: list[APIRouter] = [point.router, car_wash.router]

_all__ = ["routers"]

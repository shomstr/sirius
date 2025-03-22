from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fastapi import APIRouter

from . import point, car_wash, user, order
routers: list[APIRouter] = [point.router, car_wash.router, user.router, order.router]

_all__ = ["routers"]

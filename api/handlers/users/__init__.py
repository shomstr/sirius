from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fastapi import APIRouter

from . import point
routers: list[APIRouter] = [point.router]

_all__ = ["routers"]

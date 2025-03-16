from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fastapi import APIRouter


routers: list[APIRouter] = []

_all__ = ["routers"]

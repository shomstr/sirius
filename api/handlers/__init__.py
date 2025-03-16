from __future__ import annotations
import logging

from fastapi import FastAPI, APIRouter
from . import users

logger = logging.getLogger("handlers")

all_routers: list[APIRouter] = [*users.routers,]


def setup_routers(app: FastAPI) -> None:
    for router in all_routers:
        app.include_router(router)

    logger.debug("%s routers has been load", len(all_routers))


__all__ = [
    "setup_routers",
]

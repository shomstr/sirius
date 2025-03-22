from __future__ import annotations

from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession

from .car_wash import СarWashRepo
from .point import PointsRepo
from .users import UsersRepo, UsersOrdersRepo


@dataclass
class Repositories:
    session: AsyncSession
    users: UsersRepo
    orders: UsersOrdersRepo
    points: PointsRepo
    wash: СarWashRepo

    @staticmethod
    def get_repo(session: AsyncSession) -> Repositories:
        return Repositories(session=session, users=UsersRepo(session), orders=UsersOrdersRepo(session), points=PointsRepo(session), wash=СarWashRepo(session))


__all__ = [
    "Repositories",
]

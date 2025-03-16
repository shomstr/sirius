from __future__ import annotations

from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession

from .point import PointsRepo
from .users import UsersRepo


@dataclass
class Repositories:
    session: AsyncSession
    users: UsersRepo
    points: PointsRepo

    @staticmethod
    def get_repo(session: AsyncSession) -> Repositories:
        return Repositories(session=session, users=UsersRepo(session), points=PointsRepo(session))


__all__ = [
    "Repositories",
]

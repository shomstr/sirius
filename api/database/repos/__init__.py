from __future__ import annotations

from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession

from .users import UsersRepo


@dataclass
class Repositories:
    session: AsyncSession
    users: UsersRepo

    @staticmethod
    def get_repo(session: AsyncSession) -> Repositories:
        return Repositories(session=session, users=UsersRepo(session))


__all__ = [
    "Repositories",
]

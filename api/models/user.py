from __future__ import annotations

from datetime import datetime
from typing import Self, Sequence

from pydantic import EmailStr
from sqlalchemy import String, select, ForeignKey, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.mysql import VARCHAR, DATETIME
from models import Base


class User(Base):

    email: Mapped[str] = mapped_column(VARCHAR(100), unique=True)
    password: Mapped[str] = mapped_column(VARCHAR(100))

    @staticmethod
    async def create_user(db: AsyncSession, email: EmailStr, password: str) -> "User":
        user = User(email=email, password=password)
        db.add(user)
        await db.commit()

        return user


    @staticmethod
    async def get_user(db: AsyncSession, email: EmailStr, password: str) -> "User" | None:
        q = select(User).where(User.email==email, User.password==password)
        user = (await db.execute(q)).scalar()
        return user


    @staticmethod
    async def get_by_id(db: AsyncSession, user_id: int) -> "User" | None:
        q = select(User).where(User.id == user_id)
        user = (await db.execute(q)).scalar()
        return user


class UserFile(Base):
    fk_user: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"))
    file_name: Mapped[str] = mapped_column(VARCHAR(100))

    upload_at: Mapped[datetime] = mapped_column(server_default=func.now())


    @staticmethod
    async def create_user_file(
            db: AsyncSession,
            fk_user: int,
            file_name: str
    ) -> "UserFile":
        file = UserFile(fk_user=fk_user, file_name=file_name)
        db.add(file)
        await db.commit()

        return file

    @staticmethod
    async def get_user_uploads_files(db: AsyncSession, user_id: int) -> Sequence["UserFile"]:
        q = select(UserFile).where(UserFile.fk_user == user_id)

        files = (await db.execute(q)).scalars().all()
        return files

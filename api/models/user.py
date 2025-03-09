from __future__ import annotations

from datetime import datetime
from typing import Self, Sequence

from pydantic import EmailStr
from sqlalchemy import String, select, ForeignKey, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.postgresql import VARCHAR, BIGINT, TEXT

from models import Base


class Users_data(Base):
    __tablename__ = "users_data"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True)
    password: Mapped[str] = mapped_column(TEXT)
    name: Mapped[str] = mapped_column(TEXT)
    login: Mapped[str] = mapped_column(TEXT)
    phone: Mapped[int] = mapped_column(BIGINT)

    @staticmethod
    async def create_user(db: AsyncSession, name: str, password: str, login: str, phone: int) -> "Users_data":
        user = Users_data(name=name, password=password, login=login, phone=phone) 
        db.add(user)
        await db.commit()
        await db.refresh(user) 
        return user

    async def get_user(db: AsyncSession, phone: int, password: str = None) -> "Users_data":
        query = select(Users_data).where(Users_data.phone == phone)
        if password:
            query = query.where(Users_data.password == password)
        result = await db.execute(query)
        return result.scalars().first()


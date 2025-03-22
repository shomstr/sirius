from __future__ import annotations

from datetime import datetime
from typing import Self, Sequence

from pydantic import EmailStr
from sqlalchemy import String, select, ForeignKey, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.postgresql import VARCHAR, BIGINT, TEXT

from .base_models import Base
from .types import intpk


class User_data(Base):
    __tablename__ = "users_data"

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(TEXT)
    login: Mapped[str] = mapped_column(TEXT)

    password: Mapped[str] = mapped_column(TEXT)
    phone: Mapped[int] = mapped_column(BIGINT)

    balance: Mapped[int] = mapped_column(server_default="0")

    orders: Mapped[list["UserOrder"]] = relationship(
        lazy="selectin",
        foreign_keys="UserOrder.user_id",
        passive_deletes=True,
        cascade="all, delete",
        post_update=True,
        order_by="UserOrder.id"
    )

    @staticmethod
    async def create_user(db: AsyncSession, name: str, password: str, login: str, phone: int) -> "User_data":
        user = User_data(name=name, password=password, login=login, phone=phone)
        db.add(user)
        await db.commit()
        await db.refresh(user) 
        return user

    @staticmethod
    async def get_user(db: AsyncSession, phone: int, password: str = None) -> "User_data":
        query = select(User_data).where(User_data.phone == phone)
        if password:
            query = query.where(User_data.password == password)

        result = await db.execute(query)
        return result.scalars().first()


class UserOrder(Base):
    __tablename__ = "users_orders"

    id: Mapped[intpk]

    user_id: Mapped[int] = mapped_column(ForeignKey(User_data.id, ondelete="CASCADE"), nullable=False)

    order_amount: Mapped[int] = mapped_column(server_default="0")
    address: Mapped[str] = mapped_column(TEXT)
    fuel_load: Mapped[int] = mapped_column(server_default="0")



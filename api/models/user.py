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


class City_User(Base):
    __tablename__ = "city_user" 
    user_id: Mapped[int] = mapped_column(BIGINT, ForeignKey("users_data.id"), primary_key=True) 
    city_id: Mapped[int] = mapped_column(BIGINT, primary_key=True)

    @staticmethod
    async def add_city(db: AsyncSession, user_id: int, city_id: int) -> "City_User": 
        city = City_User(user_id=user_id, city_id=city_id) 
        db.add(city) 
        await db.commit()
        await db.refresh(city) 
        return city

class City(Base):
    name: Mapped[str] = mapped_column(TEXT) 


class Hospital(Base):
    hospital_name: Mapped[str] = mapped_column(TEXT)
    city_id: Mapped[int] = mapped_column(BIGINT, ForeignKey("city.id")) 
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


class Lab_Tests(Base):
    user_id: Mapped[int] = mapped_column(BIGINT, ForeignKey("users_data.id"))
    hospital_id: Mapped[int] = mapped_column(BIGINT, ForeignKey("hospital.id"))
    result: Mapped[str] = mapped_column(TEXT)

class Admissions(Base):
    user_id: Mapped[int] = mapped_column(BIGINT, ForeignKey("users_data.id")) # user_id как внешний ключ
    upcomming: Mapped[str] = mapped_column(TEXT)
    completed: Mapped[str] = mapped_column(TEXT)
    canselled: Mapped[str] = mapped_column(TEXT)
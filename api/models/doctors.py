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

class Doctors(Base):
    hospital_id: Mapped[int] = mapped_column(BIGINT, ForeignKey("hospital.id"))
    name: Mapped[str] = mapped_column(TEXT)
    doctor_spec_id: Mapped[int] = mapped_column(BIGINT)


class Doctor_Specialization(Base):
    specialization: Mapped[str] = mapped_column(TEXT)
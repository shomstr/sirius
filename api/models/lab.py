from .base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class Lab(Base):
    lab_id: Mapped[int] = mapped_column(primary_key=True)
    lab_name = Column(String(128))
    infect = Column(Integer)
    bio_experience = Column(Integer)

from typing import Annotated

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr

class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True)


str255 = Annotated[int, mapped_column(String(200), nullable=False)]
str128 = Annotated[int, mapped_column(String(128), nullable=False)]
str32 = Annotated[int, mapped_column(String(32), nullable=False)]
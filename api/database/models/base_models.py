from __future__ import annotations

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped

from api.database.models.mixins import ReprMixin, SerializeMixin
from api.database.models.types import intpk


class Base(DeclarativeBase, ReprMixin, SerializeMixin):
    __abstract__ = True
    ...


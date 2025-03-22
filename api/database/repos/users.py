from __future__ import annotations

from typing import Sequence
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from .base import BaseRepo
from api.database.models import User_data, UserOrder


class UsersRepo(BaseRepo):
    model = User_data


class UsersOrdersRepo(BaseRepo):
    model = UserOrder




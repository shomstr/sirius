"""test

Revision ID: 241b6d80866d
Revises: 
Create Date: 2024-10-15 23:35:05.634621

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '241b6d80866d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

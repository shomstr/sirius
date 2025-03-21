"""empty message

Revision ID: 41fbcadf6b93
Revises: 470988a7b36b
Create Date: 2024-11-06 01:03:29.909037

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '41fbcadf6b93'
down_revision: Union[str, None] = '470988a7b36b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userfile',
    sa.Column('fk_user', sa.Integer(), nullable=False),
    sa.Column('file_name', mysql.VARCHAR(), nullable=False),
    sa.Column('upload_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['fk_user'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_unique_constraint(None, 'user', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_table('userfile')
    # ### end Alembic commands ###

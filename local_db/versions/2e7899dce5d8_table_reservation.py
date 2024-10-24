"""table reservation

Revision ID: 2e7899dce5d8
Revises: 1d096bd7aa5b
Create Date: 2024-10-23 08:05:12.339982

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2e7899dce5d8'
down_revision: Union[str, None] = '1d096bd7aa5b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('review', sa.Column('at_restaurant', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'review', 'restaurant', ['at_restaurant'], ['Id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'review', type_='foreignkey')
    op.drop_column('review', 'at_restaurant')
    # ### end Alembic commands ###

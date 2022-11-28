"""removed nullable

Revision ID: bcfd7fbb962e
Revises: 4564d3585754
Create Date: 2022-11-28 09:33:10.703240

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcfd7fbb962e'
down_revision = '4564d3585754'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'techs', ['email'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'techs', type_='unique')
    # ### end Alembic commands ###
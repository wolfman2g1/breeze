"""modified the contacts table

Revision ID: 385325bb794d
Revises: 16ca85ebaf6e
Create Date: 2022-11-16 10:32:43.122890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '385325bb794d'
down_revision = '16ca85ebaf6e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contacts', sa.Column('phone', sa.String(), nullable=True))
    op.drop_column('contacts', 'password')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contacts', sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('contacts', 'phone')
    # ### end Alembic commands ###

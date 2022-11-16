"""create all tables

Revision ID: 414aec58e86c
Revises: 385325bb794d
Create Date: 2022-11-16 11:47:29.246936

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '414aec58e86c'
down_revision = '385325bb794d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('techs',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('fname', sa.String(length=50), nullable=True),
    sa.Column('lname', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tickets',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('ticket_id', sa.String(length=20), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('user_id', postgresql.UUID(), nullable=True),
    sa.Column('tech_id', postgresql.UUID(), nullable=True),
    sa.Column('customer_id', postgresql.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['tech_id'], ['techs.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['contacts.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('status'),
    sa.UniqueConstraint('ticket_id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('notes',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('public', sa.Boolean(), nullable=True),
    sa.Column('note', sa.Text(), nullable=True),
    sa.Column('entered_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('ticket_id', postgresql.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['ticket_id'], ['tickets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('contacts', sa.Column('password', sa.String(), nullable=False))
    op.add_column('contacts', sa.Column('created', sa.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False))
    op.create_unique_constraint(None, 'customers', ['customer_name'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'customers', type_='unique')
    op.drop_column('contacts', 'created')
    op.drop_column('contacts', 'password')
    op.drop_table('notes')
    op.drop_table('tickets')
    op.drop_table('techs')
    # ### end Alembic commands ###
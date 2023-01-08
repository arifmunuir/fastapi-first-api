"""add users table

Revision ID: 9f23dc8c9687
Revises: 9140ff86fd43
Create Date: 2023-01-08 16:52:17.270353

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f23dc8c9687'
down_revision = '9140ff86fd43'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
        sa.Column('id',sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.Integer(), nullable=False),
        sa.Column('create_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
        )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass

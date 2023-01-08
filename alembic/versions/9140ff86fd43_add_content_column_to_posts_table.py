"""add content column to posts table

Revision ID: 9140ff86fd43
Revises: a729ff6e7f97
Create Date: 2023-01-08 16:45:38.027417

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9140ff86fd43'
down_revision = 'a729ff6e7f97'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass

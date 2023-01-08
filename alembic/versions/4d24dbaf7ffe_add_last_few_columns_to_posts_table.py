"""add last few columns to posts table

Revision ID: 4d24dbaf7ffe
Revises: 30f780d3fe9d
Create Date: 2023-01-08 19:22:17.767517

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d24dbaf7ffe'
down_revision = '30f780d3fe9d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',
    sa.Column('published', sa.BOOLEAN(), nullable=False, server_default='TRUE'))
    op.add_column('posts',
    sa.Column('create_at', sa.TIMESTAMP(timezone=True),
              server_default=sa.text('now()'), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts","created_at")
    pass

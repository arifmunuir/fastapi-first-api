"""add foreign-key to posts table

Revision ID: 30f780d3fe9d
Revises: 9f23dc8c9687
Create Date: 2023-01-08 19:15:03.299995

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30f780d3fe9d'
down_revision = '9f23dc8c9687'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name="posts")
    op.drop_column("posts","owner_id")
    pass

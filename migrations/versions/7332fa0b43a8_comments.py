"""comments

Revision ID: 7332fa0b43a8
Revises: de0982941e6c
Create Date: 2022-02-15 11:07:32.897924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7332fa0b43a8'
down_revision = 'de0982941e6c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'comments',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id',sa.Integer, nullable=False),
        sa.Column('moto_id', sa.Integer, nullable=False),
        sa.Column('title', sa.String(20), nullable=False),
        sa.Column('comment', sa.String(120), nullable=False),
        sa.Column('date', sa.DateTime, nullable=False)
        )


def downgrade():
    op.drop_table('comments')
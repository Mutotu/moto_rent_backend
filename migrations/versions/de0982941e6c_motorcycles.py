"""motorcycles

Revision ID: de0982941e6c
Revises: 8fc3ada8052e
Create Date: 2022-02-15 11:04:40.114834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de0982941e6c'
down_revision = '8fc3ada8052e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('motorcycles',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('make', sa.String, nullable=False),
        sa.Column('model', sa.String, nullable=False),
        sa.Column('year',sa.String, nullable=False),
        sa.Column('price',sa.Float, nullable=False),
        sa.Column('description',sa.String, nullable=False),
        sa.Column('photo', sa.String, nullable=False)
                    )


def downgrade():
    op.drop_table('motorcycles')
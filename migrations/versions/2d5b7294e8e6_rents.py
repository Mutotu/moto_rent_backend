"""rents

Revision ID: 2d5b7294e8e6
Revises: 7332fa0b43a8
Create Date: 2022-02-15 11:08:58.475424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d5b7294e8e6'
down_revision = '7332fa0b43a8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'rent',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('moto_id', sa.Integer, nullable=False),
        sa.Column('start_date', sa.String, nullable=False),
        sa.Column('end_date',sa.String, nullable=False),
        sa.Column('total_price',sa.Float, nullable=False),
        sa.Column('confirmed', sa.Boolean),
        sa.Column('date', sa.DateTime, nullable=False)
       
        
    )


def downgrade():
    op.drop_table('rent')

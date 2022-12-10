"""create blogs table

Revision ID: f23595adda92
Revises: 
Create Date: 2022-12-09 14:29:19.928181

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fbdc10149a9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'blogs',
        sa.Column('id', sa.Integer, primary_key=True,unique=True),
        sa.Column('title', sa.String(50), nullable=False),
        sa.Column('body', sa.String(200)),
        # sa.Column('phone', sa.Integer(200))
    )

def downgrade() -> None:
    pass

"""create users table

Revision ID: eba0c7c1a399
Revises: 3fbdc10149a9
Create Date: 2022-12-10 10:39:12.739687

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eba0c7c1a399'
down_revision = '3fbdc10149a9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True,unique=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('email', sa.String(200)),
        sa.Column('password', sa.String(200)),
    )


def downgrade() -> None:
    pass

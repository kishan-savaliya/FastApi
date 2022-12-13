"""created schema

Revision ID: 32c4f1c1389a
Revises: 28a63482ccfb
Create Date: 2022-12-12 15:15:00.782252

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '32c4f1c1389a'
down_revision = '28a63482ccfb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('birth_date', sa.Date(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_table('competition',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_competition_id'), 'competition', ['id'], unique=False)
    op.create_table('entry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('topic', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('competition_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['competition_id'], ['competition.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_entry_id'), 'entry', ['id'], unique=False)
    op.drop_index('ix_users_table_id', table_name='users_table')
    op.drop_table('users_table')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users_table',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('birth_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('gender', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('is_delete', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='users_table_pkey')
    )
    op.create_index('ix_users_table_id', 'users_table', ['id'], unique=False)
    op.drop_index(op.f('ix_entry_id'), table_name='entry')
    op.drop_table('entry')
    op.drop_index(op.f('ix_competition_id'), table_name='competition')
    op.drop_table('competition')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
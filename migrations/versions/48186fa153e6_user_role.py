"""user-role

Revision ID: 48186fa153e6
Revises: d21ed47c66d8
Create Date: 2021-10-29 10:43:32.590698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48186fa153e6'
down_revision = 'd21ed47c66d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_role',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'role_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_role')
    # ### end Alembic commands ###

"""added about me and last seen field

Revision ID: e20164bcc24e
Revises: 32ac5ff2cd63
Create Date: 2018-10-03 19:02:01.653254

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e20164bcc24e'
down_revision = '32ac5ff2cd63'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_user_last_seen'), 'user', ['last_seen'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_last_seen'), table_name='user')
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###

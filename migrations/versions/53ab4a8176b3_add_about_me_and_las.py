"""Add about_me and last_seen to user table.

Revision ID: 53ab4a8176b3
Revises: 5abf23de97e8
Create Date: 2013-11-12 06:04:06.218006

"""

# revision identifiers, used by Alembic.
revision = '53ab4a8176b3'
down_revision = '5abf23de97e8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    ### end Alembic commands ###

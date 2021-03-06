"""add picture

Revision ID: acb63b1ad3fa
Revises: 13511506c865
Create Date: 2020-05-28 23:18:54.786833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'acb63b1ad3fa'
down_revision = '13511506c865'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('picture', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'picture')
    # ### end Alembic commands ###

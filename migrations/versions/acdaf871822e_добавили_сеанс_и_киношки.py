"""добавили сеанс и киношки

Revision ID: acdaf871822e
Revises: acb63b1ad3fa
Create Date: 2020-05-31 00:23:45.359966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'acdaf871822e'
down_revision = 'acb63b1ad3fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cinema',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=300), nullable=True),
    sa.Column('location', sa.String(length=500), nullable=True),
    sa.Column('days_work', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('session',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('session_cinema',
    sa.Column('cinema_id', sa.Integer(), nullable=True),
    sa.Column('session_id', sa.Integer(), nullable=True),
    sa.Column('time', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['cinema_id'], ['cinema.id'], ),
    sa.ForeignKeyConstraint(['session_id'], ['session.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('session_cinema')
    op.drop_table('session')
    op.drop_table('cinema')
    # ### end Alembic commands ###

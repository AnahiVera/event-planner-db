"""empty message

Revision ID: fae05a1123ab
Revises: 634fdf65d4d7
Create Date: 2025-01-05 18:39:15.326793

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fae05a1123ab'
down_revision = '634fdf65d4d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('events', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(length=120), nullable=False))
        batch_op.drop_column('tittle')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('events', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tittle', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.drop_column('title')

    # ### end Alembic commands ###
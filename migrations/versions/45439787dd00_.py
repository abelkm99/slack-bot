"""empty message

Revision ID: 45439787dd00
Revises: b89963e7ab39
Create Date: 2023-03-12 15:59:59.926485

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '45439787dd00'
down_revision = 'b89963e7ab39'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('daily_plan', schema=None) as batch_op:
        batch_op.alter_column('message_id',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)

    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('type', sa.String(length=50), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.drop_column('type')

    with op.batch_alter_table('daily_plan', schema=None) as batch_op:
        batch_op.alter_column('message_id',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)

    # ### end Alembic commands ###
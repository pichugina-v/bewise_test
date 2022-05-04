"""empty message

Revision ID: 933d781360a2
Revises: d9577e1188b3
Create Date: 2022-05-04 16:27:40.900696

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '933d781360a2'
down_revision = 'd9577e1188b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('quiz_info', schema=None) as batch_op:
        batch_op.create_unique_constraint('Question', ['question'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('quiz_info', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
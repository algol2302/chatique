"""Change role model

Revision ID: 203c75f35972
Revises: bb5c83e0b2bd
Create Date: 2021-05-22 02:30:29.064274

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '203c75f35972'
down_revision = 'bb5c83e0b2bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('role', 'role',
               existing_type=postgresql.ENUM(sa.VARCHAR(length=5)),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('role', 'role',
               existing_type=postgresql.ARRAY(sa.VARCHAR(length=5)),
               nullable=True)
    # ### end Alembic commands ###
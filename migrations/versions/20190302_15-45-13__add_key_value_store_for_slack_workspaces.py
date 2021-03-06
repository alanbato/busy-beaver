"""add key value store for slack workspaces

Revision ID: 500e1baf1bef
Revises: a5915c5a78eb
Create Date: 2019-03-02 15:45:13.600162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '500e1baf1bef'
down_revision = 'a5915c5a78eb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('key_value_store',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.Column('key', sa.String(length=255), nullable=False),
    sa.Column('value', sa.LargeBinary(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('key_value_store')
    # ### end Alembic commands ###

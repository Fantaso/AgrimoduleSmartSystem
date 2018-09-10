"""empty message

Revision ID: e03c871757fa
Revises: 
Create Date: 2018-09-03 16:09:04.564848

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e03c871757fa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('workwithustable')
    op.drop_table('platformfbtable')
    op.drop_table('newslettertable')
    op.add_column('farm', sa.Column('farm_coordinates', sa.String(length=3000), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('farm', 'farm_coordinates')
    op.create_table('newslettertable',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('_time_created', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='newslettertable_pkey')
    )
    op.create_table('platformfbtable',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('msg', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('_time_created', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='platformfbtable_pkey')
    )
    op.create_table('workwithustable',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('msg', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('_time_created', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='workwithustable_pkey')
    )
    # ### end Alembic commands ###
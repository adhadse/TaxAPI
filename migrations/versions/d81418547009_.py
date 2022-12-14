"""empty message

Revision ID: d81418547009
Revises: 
Create Date: 2022-05-24 07:38:23.747315

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils.types.email

# revision identifiers, used by Alembic.
revision = 'd81418547009'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('idx', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=25), nullable=False),
    sa.Column('email', sqlalchemy_utils.types.email.EmailType(), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.PrimaryKeyConstraint('idx'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('country',
    sa.Column('idx', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('central_tax', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('idx'),
    sa.UniqueConstraint('name')
    )
    op.create_table('taxAccountant',
    sa.Column('idx', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=25), nullable=False),
    sa.Column('email', sqlalchemy_utils.types.email.EmailType(), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.PrimaryKeyConstraint('idx'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('state',
    sa.Column('idx', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('union_territory', sa.Boolean(), nullable=False),
    sa.Column('state_tax', sa.Integer(), nullable=False),
    sa.Column('country_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['country_id'], ['country.idx'], ),
    sa.PrimaryKeyConstraint('idx'),
    sa.UniqueConstraint('name')
    )
    op.create_table('taxPayer',
    sa.Column('idx', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=25), nullable=False),
    sa.Column('email', sqlalchemy_utils.types.email.EmailType(), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.Column('country_id', sa.Integer(), nullable=True),
    sa.Column('state_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.ForeignKeyConstraint(['country_id'], ['country.idx'], ),
    sa.ForeignKeyConstraint(['state_id'], ['state.idx'], ),
    sa.PrimaryKeyConstraint('idx'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('taxPayer')
    op.drop_table('state')
    op.drop_table('taxAccountant')
    op.drop_table('country')
    op.drop_table('admin')
    # ### end Alembic commands ###

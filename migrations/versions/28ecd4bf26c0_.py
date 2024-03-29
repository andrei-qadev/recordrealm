"""empty message

Revision ID: 28ecd4bf26c0
Revises: 
Create Date: 2023-03-19 21:21:31.564380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28ecd4bf26c0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('role', sa.Enum('user', name='roletype'), server_default='user', nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    schema='user_data'
    )
    op.create_table('collections',
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('release_id', sa.Integer(), nullable=False),
    sa.Column('condition', sa.Enum('poor', 'good', 'very_good', 'very_good_p', 'excellent', 'near_mint', 'mint', name='conditiontype'), nullable=False),
    sa.Column('bought_for', sa.Integer(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('is_for_sale', sa.Boolean(), server_default='false', nullable=True),
    sa.Column('is_sold', sa.Boolean(), server_default='false', nullable=True),
    sa.Column('sold_for', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user_data.users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='user_data'
    )
    op.create_table('wishlists',
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('release_id', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user_data.users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='user_data'
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wishlists', schema='user_data')
    op.drop_table('collections', schema='user_data')
    op.drop_table('users', schema='user_data')
    # ### end Alembic commands ###

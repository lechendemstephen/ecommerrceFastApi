"""empty message

Revision ID: 0c21591dd5ae
Revises: 8eed667fdec2
Create Date: 2024-09-16 23:25:54.465834

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0c21591dd5ae'
down_revision: Union[str, None] = '8eed667fdec2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('jioned_date', sa.TIMESTAMP(timezone=True), server_default='now()', nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('blog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('created_date', sa.TIMESTAMP(timezone=True), server_default='now()', nullable=False),
    sa.Column('post_owner', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_owner'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('created_date', sa.TIMESTAMP(timezone=True), server_default='now()', nullable=False),
    sa.Column('post_owner', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_owner'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    op.drop_table('blog')
    op.drop_table('users')
    # ### end Alembic commands ###

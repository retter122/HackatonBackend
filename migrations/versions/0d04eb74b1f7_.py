"""empty message

Revision ID: 0d04eb74b1f7
Revises: 
Create Date: 2024-08-03 21:05:59.372932

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0d04eb74b1f7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('mail', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tutorial',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('creator_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['creator_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('like', sa.Boolean(), nullable=False),
    sa.Column('dislike', sa.Boolean(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('creator_id', sa.Integer(), nullable=False),
    sa.Column('source_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['creator_id'], ['user.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['source_id'], ['tutorial.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('module',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('document', sa.String(), nullable=False),
    sa.Column('source_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['source_id'], ['tutorial.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tag_type', sa.Enum('backend', 'frontend', 'fullstack', 'gamedev', 'design', 'modeling3d', 'bas', 'business', name='tagtype'), nullable=False),
    sa.Column('source_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['source_id'], ['tutorial.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tag')
    op.drop_table('module')
    op.drop_table('comment')
    op.drop_table('tutorial')
    op.drop_table('user')
    # ### end Alembic commands ###
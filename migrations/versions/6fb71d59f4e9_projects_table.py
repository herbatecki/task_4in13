"""projects table

Revision ID: 6fb71d59f4e9
Revises: 
Create Date: 2021-12-05 22:53:25.217002

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6fb71d59f4e9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('start_date', sa.String(length=200), nullable=True),
    sa.Column('end_date', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_project_name'), 'project', ['name'], unique=True)
    op.drop_table('projects')
    op.drop_table('tasks')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tasks',
    sa.Column('id', sa.INTEGER(), nullable=True),
    sa.Column('project_id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=250), nullable=False),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.Column('status', sa.VARCHAR(length=15), nullable=False),
    sa.Column('start_date', sa.TEXT(), nullable=False),
    sa.Column('end_date', sa.TEXT(), nullable=False),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('projects',
    sa.Column('id', sa.INTEGER(), nullable=True),
    sa.Column('name', sa.TEXT(), nullable=False),
    sa.Column('start_date', sa.TEXT(), nullable=True),
    sa.Column('end_date', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index(op.f('ix_project_name'), table_name='project')
    op.drop_table('project')
    # ### end Alembic commands ###
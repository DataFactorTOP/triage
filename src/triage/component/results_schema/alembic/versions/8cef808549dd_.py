"""empty message

Revision ID: 8cef808549dd
Revises: b4d7569d31cb
Create Date: 2020-06-02 21:26:32.528991

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8cef808549dd'
down_revision = 'b4d7569d31cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('experiment_runs', sa.Column('python_version', sa.String(), nullable=True), schema='model_metadata')
    op.create_index(op.f('ix_model_metadata_models_model_hash'), 'models', ['model_hash'], unique=True, schema='model_metadata')
    op.drop_index('ix_results_models_model_hash', table_name='models', schema='model_metadata')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_results_models_model_hash', 'models', ['model_hash'], unique=True, schema='model_metadata')
    op.drop_index(op.f('ix_model_metadata_models_model_hash'), table_name='models', schema='model_metadata')
    op.drop_column('experiment_runs', 'python_version', schema='model_metadata')
    # ### end Alembic commands ###

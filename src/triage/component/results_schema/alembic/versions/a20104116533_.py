"""empty message

Revision ID: a20104116533
Revises: 8cef808549dd
Create Date: 2020-06-11 16:32:41.319128

"""
import os
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a20104116533'
down_revision = '8cef808549dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("CREATE SCHEMA IF NOT EXISTS triage_metadata")
    op.execute(
        "ALTER TABLE model_metadata.experiment_matrices SET SCHEMA triage_metadata;"
        + " ALTER TABLE model_metadata.experiment_models SET SCHEMA triage_metadata;"
        + " ALTER TABLE model_metadata.experiment_runs SET SCHEMA triage_metadata;"
        + " ALTER TABLE model_metadata.experiments SET SCHEMA triage_metadata;"
        + " ALTER TABLE model_metadata.list_predictions SET SCHEMA triage_metadata;"
        + " ALTER TABLE model_metadata.matrices SET SCHEMA triage_metadata;"
        + " ALTER TABLE model_metadata.model_groups SET SCHEMA triage_metadata;"
        + " ALTER TABLE model_metadata.models SET SCHEMA triage_metadata;"
        + " ALTER TABLE model_metadata.subsets SET SCHEMA triage_metadata;"
    )

    op.execute("DROP SCHEMA IF EXISTS model_metadata")

    ## We update (replace) the function
    group_proc_filename = os.path.join(
        os.path.dirname(__file__), "../../model_group_stored_procedure.sql"
    )
    with open(group_proc_filename) as fd:
        stmt = fd.read()
        op.execute(stmt)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("CREATE SCHEMA IF NOT EXISTS model_metadata")

    op.execute(
        "ALTER TABLE triage_metadata.experiment_matrices SET SCHEMA model_metadata;"
        + " ALTER TABLE triage_metadata.experiment_models SET SCHEMA model_metadata;"
        + " ALTER TABLE triage_metadata.experiment_runs SET SCHEMA model_metadata;"
        + " ALTER TABLE triage_metadata.experiments SET SCHEMA model_metadata;"
        + " ALTER TABLE triage_metadata.matrices SET SCHEMA model_metadata;"
        + " ALTER TABLE triage_metadata.model_groups SET SCHEMA model_metadata;"
        + " ALTER TABLE triage_metadata.models SET SCHEMA model_metadata;"
        + " ALTER TABLE triage_metadata.subsets SET SCHEMA model_metadata;"
    )

    # ### end Alembic commands ###

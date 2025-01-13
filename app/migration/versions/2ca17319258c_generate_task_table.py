"""generate task table

Revision ID: 2ca17319258c
Revises: 5db428e0ebee
Create Date: 2025-01-09 16:45:34.761077

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from schemas.base_entity import Status, Priority


# revision identifiers, used by Alembic.
revision: str = '2ca17319258c'
down_revision: Union[str, None] = '5db428e0ebee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "tasks",
        sa.Column("id", sa.UUID, nullable=False, primary_key=True),
        sa.Column("summary", sa.String, nullable=False),
        sa.Column("description", sa.String, nullable=False),
        sa.Column("status", sa.Enum(Status), nullable=False, default=Status.OPEN),
        sa.Column("priority", sa.Enum(Priority), nullable=False, default=Priority.MEDIUM),
        sa.Column("reporter_id", sa.UUID, nullable=False),
        sa.Column("assignee_id", sa.UUID),
        sa.Column("created_at", sa.DateTime),
        sa.Column("updated_at", sa.DateTime),
    )

    op.create_foreign_key("fk_task_reporter", "tasks", "users", ["reporter_id"], ["id"])
    op.create_foreign_key("fk_task_assignee", "tasks", "users", ["assignee_id"], ["id"])


def downgrade() -> None:
    op.drop_table("tasks")
    op.execute("DROP TYPE Status;")
    op.execute("DROP TYPE Priority;")

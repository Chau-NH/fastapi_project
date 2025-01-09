"""generate user table

Revision ID: 5db428e0ebee
Revises: 688895df1590
Create Date: 2025-01-07 15:12:53.007683

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5db428e0ebee'
down_revision: Union[str, None] = '688895df1590'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.UUID, nullable=False, primary_key=True),
        sa.Column("email", sa.String, unique=True, index=True),
        sa.Column("username", sa.String, unique=True, nullable=False, index=True),
        sa.Column("password", sa.String, nullable=False),
        sa.Column("first_name", sa.String),
        sa.Column("last_name", sa.String),
        sa.Column("is_active", sa.Boolean, default=True),
        sa.Column("is_admin", sa.Boolean, default=False),
        sa.Column("company_id", sa.UUID, nullable=True),
        sa.Column("created_at", sa.DateTime),
        sa.Column("updated_at", sa.DateTime),
    )

    op.create_index("idx_usr_fst_lst_name", "users", ["first_name", "last_name"])
    op.create_foreign_key("fk_user_company", "users", "companies", ["company_id"], ["id"])


def downgrade() -> None:
    op.drop_table("users")

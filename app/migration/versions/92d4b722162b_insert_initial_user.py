"""insert initial user

Revision ID: 92d4b722162b
Revises: 2ca17319258c
Create Date: 2025-01-13 10:54:21.112003

"""
from typing import Sequence, Union
from uuid import uuid4
from datetime import datetime, timezone

from alembic import op
from sqlalchemy.sql import table, column
from sqlalchemy import String, Boolean, DateTime

from utility import user as user_util
from settings import ADMIN_DEFAULT_PASSWORD


# revision identifiers, used by Alembic.
revision: str = '92d4b722162b'
down_revision: Union[str, None] = '2ca17319258c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# Define the table structure
users_table = table(
    'users',
    column('id', String),
    column('email', String),
    column('username', String),
    column('password', String),
    column('first_name', String),
    column('last_name', String),
    column('is_active', Boolean),
    column('is_admin', Boolean),
    column('created_at', DateTime),
    column('updated_at', DateTime)
)

def upgrade() -> None:
    insert_data = {
        "id": str(uuid4()),  # Ensure the UUID is converted to a string
        "email": "admin@sample.com",
        "username": "admin",
        "password": user_util.get_password_hash(ADMIN_DEFAULT_PASSWORD),
        "first_name": "FastAPI",
        "last_name": "Admin",
        "is_active": True,
        "is_admin": True,
        "created_at": datetime.now(timezone.utc),
        "updated_at": datetime.now(timezone.utc)
    }

    op.execute(users_table.insert().values(insert_data))

def downgrade() -> None:
    op.execute(users_table.delete().where(users_table.c.username == 'admin'))

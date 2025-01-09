import os
from dotenv import load_dotenv

load_dotenv()

def get_connection_string():
    db_engine = os.environ.get('DB_ENGINE')
    db_host = os.environ.get('DB_HOST')
    db_username = os.environ.get('DB_USERNAME')
    db_password = os.environ.get('DB_PASSWORD')
    db_name = os.environ.get('DB_NAME')

    return f"{db_engine}://{db_username}:{db_password}@{db_host}/{db_name}"

# Database settings
SQLALCHEMY_DB_URL = get_connection_string()
ADMIN_DEFAULT_PASSWORD = os.environ.get("ADMIN_DEFAULT_PASSWORD")

# JWT settings
JWT_SECRET = os.environ.get("JWT_SECRET")
JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM")
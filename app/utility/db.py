from database import LocalSession

def get_db_context():
    try:
        db = LocalSession()
        yield db
    finally:
        db.close()

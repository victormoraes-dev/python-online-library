from database_config.database_configuration import SessionLocal
from sqlalchemy.orm import Session

def get_db():
    """
    Dependency that provides a database session for each request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  # Ensure the session is closed after use    
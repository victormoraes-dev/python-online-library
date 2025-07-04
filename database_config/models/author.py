from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone
from database_config.database_configuration import Base

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    description = Column(String(400), nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)

    def __repr__(self):
        return f"<Author(name={self.name}, email={self.email}, description={self.description})>"
    
    class Config: 
        orm_mode = True

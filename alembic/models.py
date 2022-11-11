from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP, text, JSON
from sqlalchemy.dialects.postgresql import UUID
import uuid
Base = declarative_base()
metadata = Base.metadata

class Customer(Base):
    __tablename__ = "companies"
    id = Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4)
    company_name = Column(String(50))
    street = Column(String(50))
    state = Column(String(50))
    postal = Column(String(10))
    created = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP") )
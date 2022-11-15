from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP, text, JSON, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
Base = declarative_base()
metadata = Base.metadata

class Customer(Base):
    __tablename__ = "customers"
    id = Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4)
    customer_name = Column(String(50))
    street = Column(String(50))
    state = Column(String(50))
    postal = Column(String(10))
    created = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP") )
    contacts = relationship('Contacts')

class Contacts(Base):
     __tablename__ = "contacts"
     id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
     fname = Column(String)
     lname = Column(String)
     email = Column(String)
     password = Column(String, nullable=False)
     customer_id = Column(UUID, ForeignKey("customers.id"))



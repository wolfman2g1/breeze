from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP, text, JSON, ForeignKey, Boolean, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
Base = declarative_base()
metadata = Base.metadata

class Customer(Base):
    __tablename__ = "customers"
    id = Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4)
    customer_name = Column(String(50),unique=True)
    street = Column(String(50))
    state = Column(String(50))
    postal = Column(String(10))
    created = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("CURRENT_TIMESTAMP") )
    contacts = relationship('Contacts')
    tickets = relationship('Tickets')
    user = relationship("Users")

class Contacts(Base):
     __tablename__ = "contacts"
     id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
     fname = Column(String(50))
     lname = Column(String(50))
     email = Column(String(50))
     phone = Column(String(11))
     password = Column(String,nullable=False)
     created = Column(TIMESTAMP(timezone=True), nullable=False,server_default=text("CURRENT_TIMESTAMP"))
     customer_id = Column(UUID, ForeignKey("customers.id"))
     tickets = relationship("Tickets")

class Notes(Base):
    __tablename__ = "notes"
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    public = Column(Boolean, nullable=True)
    note = Column(Text)
    entered_at =  Column(TIMESTAMP(timezone=True), nullable=False,server_default=text("CURRENT_TIMESTAMP"))
    ticket_id = Column(UUID, ForeignKey("tickets.id"))


class Tickets(Base):
    __tablename__ = "tickets"
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    ticket_id = Column(String(20), unique=True, nullable=False)
    title = Column(String(50), unique=True, nullable=False)
    desc = Column(Text)
    status = Column(String(50), unique=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False,server_default=text("CURRENT_TIMESTAMP"))
    updated_at =Column(TIMESTAMP(timezone=True), nullable=True,server_default=text("CURRENT_TIMESTAMP"))
    user_id = Column(UUID, ForeignKey("contacts.id"))
    tech_id = Column(UUID, ForeignKey("techs.id"))
    customer_id = Column(UUID, ForeignKey("customers.id"))
    notes = relationship("Notes")

class Techs(Base):
    __tablename__ = "techs"
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    fname = Column(String(50))
    lname = Column(String(50))
    email = Column(String(50))
    password = Column(String,nullable=False)
    admin = Column(Boolean, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False,server_default=text("CURRENT_TIMESTAMP"))
    tickets = relationship('Tickets')




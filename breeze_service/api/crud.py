from typing import Optional
import uuid
from sqlalchemy.orm import Session
from breeze_service import models
from breeze_service.api import schema


### Customer Crud ###
def get_customers_inner(db: Session, limit: int = 10, search: Optional[str] = "", skip: int = 0):
    return db.query(models.Customer).filter(models.Customer.customer_name.contains(search)).limit(limit).offset(
        skip).all()


def get_customer_by_id_inner(id: uuid.UUID, db: Session):
    return db.query(models.Customer).filter(models.Customer.id == id).first()


def get_customer_contacts_inner(db: Session, id: uuid.UUID):
    contacts = db.query(models.Customer).filter(models.Customer.id == id)
    return contacts.filter(models.Customer.contacts).all()


def update_customer_inner(db: Session, id: uuid.UUID, update: schema.Company):
    search = db.query(models.Customer).filter(models.Customer.id == id)
    search.update(update.dict())
    db.commit()
    return search.first()


def create_customer_inner(db: Session, customer: schema.Company):
    new_cust = models.Customer(**customer.dict())
    db.add(new_cust)
    db.commit()
    db.refresh(new_cust)
    return new_cust


""" Check if this customer already exists"""


def get_customer_by_name(db: Session, name: str):
    return db.query(models.Customer).filter(models.Customer.customer_name == name).first()


def delete_customer(db: Session, id: uuid.UUID):
    customer = db.query(models.Customer).filter(models.Customer.id == id)
    customer.delete()
    db.commit()


#######

### Contacts ###


def get_contact_by_id_inner(id: uuid.UUID, db: Session):
    return db.query(models.Contacts).filter(models.Contacts.id == id).first()


def check_contact_email(db: Session):
    return db.query(models.Contacts).filter(models.Contacts.email).first()


def create_contact_inner(db: Session, contact: schema.Contacts):
    new_cont = models.Contacts(**contact.dict())
    db.add(new_cont)
    db.commit()
    db.refresh(new_cont)
    return new_cont


def update_contact_inner(db: Session, id: uuid.UUID, update: schema.ContactsOut):
    search = db.query(models.Contacts).filter(models.Contacts.id == id)
    search.update(update.dict())
    db.commit()
    return search.first()


def get_contacts_inner(db: Session, limit: int = 10, search: Optional[str] = "", skip: int = 0):
    return db.query(models.Contacts).filter(models.Contacts.email.contains(search)).limit(limit).offset(skip).all()


def delete_contact(db: Session, id: uuid.UUID):
    customer = db.query(models.Contacts).filter(models.Contacts.id == id)
    customer.delete()
    db.commit()


##### Techs ###


def get_tech_by_email(db: Session, email : str):
    return db.query(models.Techs).filter(models.Techs.email == email).first()


def create_tech_inner(db: Session, tech: schema.Tech):
    new_tech = models.Techs(**tech.dict())
    db.add(new_tech)
    db.commit()
    return new_tech


def get_all_techs_inner(db: Session, limit: int = 10, search: Optional[str] = "", skip: int = 0):
    return db.query(models.Techs).filter(models.Techs.email.contains(search)).limit(limit).offset(skip).all()


def update_tech_by_id_inner(db: Session, id: uuid.UUID, update: schema.TechOut):
    search = db.query(models.Techs).filter(models.Techs.id == id)
    search.update(**update.dict())
    db.commit()
    return search.first()

def delete_tech_inner(db: Session, id: uuid.UUID):
    tech = db.query(models.Techs).filter(models.Techs.id == id)
    tech.delete()
    db.commit()

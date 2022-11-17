from typing import Optional
import uuid
from sqlalchemy.orm import Session
from breeze_service import models
from breeze_service.api import schema


### Customer Crud ###
def get_customers_inner(db: Session, limit: int = 10, search: Optional[str] = ""):
    return db.query(models.Customer).filter(models.Customer.customer_name.constraints(search).limit(limit).all())


def get_customer_by_id_inner(id: uuid.UUID, db: Session):
    return db.query(models.Customer).filter(models.Customer.id == id).first()


def get_customer_contacts_inner(id: uuid.UUID, db: Session):
    return db.query(models.Customer).filter(models.Customer.id == id).first()


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

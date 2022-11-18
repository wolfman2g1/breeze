from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
import logging
import uuid
from sqlalchemy.orm import Session
from breeze_service import models
from breeze_service.api import schema, crud
from breeze_service.database import get_db
from breeze_service.utils import hash

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/contacts", tags=["contacts"])


@router.get("/", status_code=status.HTTP_200_OK,)
def list_contacts(cust: schema.ContactsOut, db: Session = Depends(get_db), limit: int = 10, search: Optional[str] = ""):
    """ Returns a list of all contacts by  Company """
    logger.info("Getting all Contacts")
    cust = crud.get_contacts_inner(db, limit, search)
    return cust.append(cust)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.ContactsOut)
def create_contact(contact: schema.Contacts, db: Session = Depends(get_db)):
    cust_check = crud.check_contact_email(db, contact.email)
    if cust_check:
        logger.error(
            f"Customer with name {contact.email}, already Exists")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Customer with name {contact.email}, already Exists")
    hashed_pwd = hash(contact.password)
    contact.password = hashed_pwd
    logger.info(
        f"Created new contact {contact.fname},{contact.lname}. Company {contact.customer_id} ")
    return crud.create_contact_inner(db, contact)


@router.put("/{{id}}", status_code=status.HTTP_200_OK, response_model=schema.ContactsOut)
def update_contact(id: uuid.UUID, update: schema.Contacts, db: Session = Depends(get_db)):
    """ Update Contact by ID"""
    contact_query = crud.get_contact_by_id_inner(id, db)
    if contact_query == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Contact with id {id} not found")
    logger.info(f"Updated: {update.customer_name}")
    return crud.update_contact_inner(db, id, update=update)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer_by_id(id: uuid.UUID, db: Session = Depends(get_db)):
    """ Deletes a Customer"""
    customer = crud.get_customer_by_id_inner(id=id, db=db)
    if customer == None:
        logger.error(f"Contact with {id} doesn't exist")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Contact with {id} doesn't exist")
    crud.delete_contact(db=db, id=id)
    logger.info(f"Deleted Customer {customer}")
    return status.HTTP_204_NO_CONTENT

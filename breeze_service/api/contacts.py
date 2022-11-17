from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
import logging, uuid
from sqlalchemy.orm import Session
from breeze_service import models
from breeze_service.api import schema
from breeze_service.database import get_db
from breeze_service.utils import hash

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/contacts", tags=["contacts"])

@router.get("/", status_code=status.HTTP_200_OK,  )
async def list_contacts(db: Session = Depends(get_db), limit: int = 10, search: Optional[str]= ""):
    """ Returns a list of all contacts by  Company """
    logger.info("Getting all Contacts")
    contacts = db.query(models.Contacts).all()
    return contacts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.ContactsOut)
async def create_contact(contact: schema.Contacts, db: Session = Depends(get_db)):
    hashed_pwd = hash(contact.password)
    contact.password = hashed_pwd
    contact = models.Contacts(**contact.dict())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    logger.info(f"Created new contact {contact.fname},{contact.lname}. Company {contact.customer_id} ")
    return contact
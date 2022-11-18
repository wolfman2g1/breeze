from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
import logging
import uuid
from sqlalchemy.orm import Session
from breeze_service import models
from breeze_service.api import schema
from breeze_service.api import crud
from breeze_service.database import get_db

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/customers", tags=['customers'])


@router.get("/", status_code=status.HTTP_200_OK)
def list_company(db: Session = Depends(get_db), limit: int = 10, search: Optional[str] = ""):
    """ Returns a list of all customers """
    logger.info("Getting all Customers")

    return crud.get_customers_inner(db=db, search=search, limit=limit)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schema.CompanyResponse)
def get_customer_by_id(id: uuid.UUID, db: Session = Depends(get_db)):
    """ Find a customer by ID"""
    customer = crud.get_customer_by_id_inner(id=id, db=db)
    if not customer:
        logger.error(f"Customer with {id} doesn't exist")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Customer with {id} doesn't exist")
    return customer


@router.get('/{id}/contacts', status_code=status.HTTP_200_OK, response_model=schema.CompanyContactsOut)
def get_customer_contacts(id: uuid.UUID, customer: schema.CompanyResponse, db: Session = Depends(get_db)):
    """ Get a list of all company contacts by company id"""
    cust_contacts = crud.get_customer_contacts_inner(db, id)
    cust_contacts.append(**customer.dict())
    if not cust_contacts:
        logger.error(f"Customer with {id} doesn't exist")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Customer with {id} doesn't exist")
    return cust_contacts


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.Company)
def create_company(customer: schema.Company, db: Session = Depends(get_db)):
    """ Create a new customer"""
    cust_check = crud.get_customer_by_name(db, name=customer.customer_name)
    if cust_check:
        logger.error(
            f"Customer with name {customer.customer_name}, already Exists")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Customer with name {customer.customer_name}, already Exists")
    logger.info(f"Create new Customer {customer.customer_name} ")
    return crud.create_customer_inner(db, customer=customer)


@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=schema.Company)
def update_customer_by_id(id: uuid.UUID, update: schema.Company, db: Session = Depends(get_db)):
    """ Update Customer by ID"""
    customer_query = crud.get_customer_by_id_inner(id=id, db=db)
    if customer_query == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Contact with id {id} not found")
    logger.info(f"Updated: {update.customer_name}")
    return crud.update_customer_inner(db=db, id=id, update=update)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer_by_id(id: uuid.UUID, db: Session = Depends(get_db)):
    """ Deletes a Customer"""
    customer = crud.get_customer_by_id_inner(id=id, db=db)
    if customer == None:
        logger.error(f"Customer with {id} doesn't exist")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    crud.delete_customer(db=db, id=id)
    logger.info(f"Deleted Customer {customer}")
    return status.HTTP_204_NO_CONTENT

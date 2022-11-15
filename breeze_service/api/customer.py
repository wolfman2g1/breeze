from fastapi import APIRouter, Depends, HTTPException, status
import logging, uuid
from sqlalchemy.orm import Session
from breeze_service import models
from breeze_service.api import schema
from breeze_service.database import get_db

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/customers")


@router.get("/", status_code=status.HTTP_200_OK )
async def list_company(db: Session = Depends(get_db)):
    """ Returns a list of all customers """
    logger.info("Getting all Customers")
    customer =  db.query(models.Customer).all()
    return customer


@router.post("/", status_code=status.HTTP_201_CREATED ,response_model=schema.Company)
async def create_company(customer: schema.Company ,db: Session = Depends(get_db)):
    """ Create a new customer"""
    customer = models.Customer(**customer.dict())
    db.add(customer)
    db.commit()
    db.refresh(customer)
    logger.info(f"Create new Customer {customer.customer_name} ")
    return customer


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schema.CompanyResponse )
async def get_customer_by_id(id: uuid.UUID, db: Session = Depends(get_db)):
    """ Find a customer by ID"""
    customer = db.query(models.Customer).filter(models.Customer.id==id).first()
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Customer with {id} doesn't exist")
    return customer



@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=schema.Company)
async def update_customer_by_id(id: uuid.UUID, update: schema.Company, db: Session = Depends(get_db)):
    """ Update Customer by ID"""
    customer_query = db.query(models.Customer).filter(models.Customer.id == id)
    if customer_query == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Customer with {id} doesn't exist")
    customer_query.update(update.dict())
    db.commit()
    logger.info(f"Updated {update.customer_name}")
    return customer_query.first()

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_customer_by_id(id: uuid.UUID, db: Session = Depends(get_db)):
    """ Deletes a Customer"""
    customer = db.query(models.Customer).filter(models.Customer.id == id)

    if customer == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Customer with {id} doesn't exist")
    customer.delete()
    db.commit()
    logger.info(f"Deleted Customer {customer}")
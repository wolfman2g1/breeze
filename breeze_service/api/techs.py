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

router = APIRouter(prefix="/api/v1/techs", tags=['techs'])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.TechOut)
def create_tech(tech: schema.Tech, db: Session = Depends(get_db)):
    """ Create a new Tech"""
    tech_check = crud.get_tech_by_email(db, tech=tech.email)
    if tech_check:
        logger.error(
            f"Tech with email {tech.email}, already Exists")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Customer with name {tech.email}, already Exists")
    logger.info(f"Created new tech {tech.fname}, {tech.lname} ")


@router.get("/", status_code=status.HTTP_200_OK)
def get_techs(db: Session = Depends(get_db), limit: int = 10, search: Optional[str] = ""):
    """ Returns all Techs"""
    logger.info("Getting All Techs")
    return crud.get_all_techs_inner(db, search=search, limit=limit)

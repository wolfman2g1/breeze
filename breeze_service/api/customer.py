from fastapi import APIRouter
import logging
from schema import Company
from models import Customer

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1")


@router.get("/", response_model=Company)
def list_company(company: Company):
    """ Returns a list of all customers """
    logger.info()
    customer = Customer.query





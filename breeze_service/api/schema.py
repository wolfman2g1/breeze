import datetime
import uuid
from pydantic import BaseModel

class Company(BaseModel):
    customer_name: str
    street: str
    state: str
    postal: str
    class Config:
        orm_mode = True



class CompanyResponse(BaseModel):
    id: uuid.UUID
    customer_name: str
    street: str
    state: str
    postal: str
    created: datetime.datetime

    class Config:
        orm_mode = True
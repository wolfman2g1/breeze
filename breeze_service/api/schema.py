import datetime
import uuid
from pydantic import BaseModel, EmailStr


class CompanyContact(BaseException):
    pass


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


class Contacts(BaseModel):
    fname: str
    lname: str
    email: EmailStr
    password: str
    phone: str
    customer_id: uuid.UUID

    class Config:
        orm_mode = True


class ContactsOut(BaseModel):
    fname: str
    lname: str
    email: EmailStr
    created: datetime.datetime
    customer_id: uuid.UUID
    customer: CompanyResponse

    class Config:
        orm_mode = True


class CompanyContactsOut(BaseModel):
    customer_name: CompanyResponse
    contacts: ContactsOut

    class Config:
        orm_mode = True

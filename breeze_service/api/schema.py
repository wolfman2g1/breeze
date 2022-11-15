from pydantic import BaseModel

class Company(BaseModel):
    customer_name: str
    street: str
    state: str
    postal: str
    class Config:
        orm_mode = True
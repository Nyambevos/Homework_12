from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr

class ContactModel(BaseModel):
    firstname: str = Field(max_length=30)
    lastname: str = Field(max_length=30)
    email: EmailStr
    phone: str = Field(max_length=15)
    birthday: date

class ContactResponse(ContactModel):
    id: int

    class Config:
        orm_mode = True

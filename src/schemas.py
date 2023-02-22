from datetime import date as birth_date

from pydantic import BaseModel, Field, EmailStr


class ContactModel(BaseModel):
    first_name: str = Field(min_length=2, max_length=15)
    last_name: str = Field(min_length=2, max_length=15)
    email: EmailStr
    phone: str = Field(min_length=6, max_length=16)
    birthday: birth_date
    additional_info: str = Field(min_length=3, max_length=300)


class ContactResponse(BaseModel):
    id: int
    first_name: str = "Andrew"
    last_name: str = "Lastname"
    email: EmailStr = "andrew.lastname@gmail.com"
    phone: str = "+380958745896"
    birthday: birth_date = birth_date(year=1986, month=2, day=28)
    additional_info: str = "some info"

    class Config:
        orm_mode = True
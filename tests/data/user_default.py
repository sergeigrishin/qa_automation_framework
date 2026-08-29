from pydantic import BaseModel, EmailStr


class User(BaseModel):
    name: str
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    address: str
    state: str
    city: str
    zipcode: str
    mobile_number: str

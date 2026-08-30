from pydantic import BaseModel, EmailStr, Field
from faker import Faker

fake = Faker()


class User(BaseModel):
    name: str = Field(default_factory=fake.name)
    email: EmailStr = Field(default_factory=fake.email)
    password: str = Field(default_factory=lambda: fake.password(length=10))
    first_name: str = Field(default_factory=fake.first_name)
    last_name: str = Field(default_factory=fake.last_name)
    address: str = Field(default_factory=fake.address)
    state: str = Field(default_factory=fake.state)
    city: str = Field(default_factory=fake.city)
    zipcode: str = Field(default_factory=fake.zipcode)
    mobile_number: str = Field(default_factory=fake.phone_number)

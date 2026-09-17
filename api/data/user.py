from pydantic import BaseModel, EmailStr, Field
from faker import Faker

fake = Faker()


class User(BaseModel):
    name: str = Field(default_factory=fake.name)
    email: EmailStr = Field(default_factory=lambda: f"{fake.uuid4()}@test.com")
    password: str = Field(default_factory=lambda: fake.password(length=10))
    title: str = 'Mr'
    first_name: str = Field(default_factory=fake.first_name)
    last_name: str = Field(default_factory=fake.last_name)
    address: str = Field(default_factory=fake.address)
    state: str = Field(default_factory=fake.state)
    city: str = Field(default_factory=fake.city)
    zipcode: str = Field(default_factory=fake.zipcode)
    mobile_number: str = Field(default_factory=fake.phone_number)
    birth_date: str = "10"
    birth_month: str = "5"
    birth_year: str = "1995"
    company: str = "Test Company"
    country: str = "United States"
    address2: str = ""
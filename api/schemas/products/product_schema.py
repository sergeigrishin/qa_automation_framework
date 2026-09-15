from pydantic import BaseModel


class UserType(BaseModel):
    usertype: str


class Category(BaseModel):
    usertype: UserType
    category: str


class Product(BaseModel):
    id: int
    name: str
    price: str
    brand: str
    category: Category


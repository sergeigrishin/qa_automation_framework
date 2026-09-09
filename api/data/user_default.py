from pydantic import BaseModel


class UserDefault(BaseModel):
    name: str = "Petr"
    email: str = "petr_user@mail.com"
    password: str = "123Qwer!"


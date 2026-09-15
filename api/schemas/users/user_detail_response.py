from pydantic import Field, BaseModel


class UserDetails(BaseModel):
    id: int
    name: str
    email: str
    title: str
    birth_day: str
    birth_month: str
    birth_year: str
    first_name: str
    last_name: str
    company: str
    address: str = Field(alias="address1")
    address2: str
    country: str
    state: str
    city: str
    zipcode: str

class UserDetailResponse(BaseModel):
    response_code: int = Field(alias='responseCode')
    user: UserDetails
from pydantic import BaseModel, Field


class UserResponse(BaseModel):
    response_code: int = Field(alias='responseCode')
    message: str
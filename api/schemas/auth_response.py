from pydantic import BaseModel, Field


class AuthResponse(BaseModel):
    response_code: int = Field(alias="responseCode")
    message: str


class CreateAccountResponse(BaseModel):
    response_code: int = Field(alias="responseCode")
    message: str
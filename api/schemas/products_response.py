from pydantic import BaseModel, Field
from api.schemas.product_schema import Product


class ProductsResponse(BaseModel):
    response_code: int = Field(alias='responseCode')
    products: list[Product]

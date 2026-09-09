from api.clients.public_client import PublicAPIClient
from api.models.api_response import APIResponse

from api.schemas.products_response import ProductsResponse


class ProductsClient:
    """
    Клиент для работы с productsList
    """

    def __init__(self, client: PublicAPIClient):
        self.client = client

    def get_all_products(self) -> APIResponse[ProductsResponse]:
        response = self.client.get("/productsList")
        return self.client.parse_response(response, ProductsResponse)

    def search_product(self, search_product: str) -> APIResponse[ProductsResponse]:
        response = self.client.post("/searchProduct", data={"search_product": search_product})
        return self.client.parse_response(response, ProductsResponse)

    def search_product_without_query(self) -> APIResponse[dict]:
        response = self.client.post("/searchProduct")
        return APIResponse(status_code=response.status_code, data=response.json())

    

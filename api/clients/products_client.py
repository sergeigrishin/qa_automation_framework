from api.clients.api_client import APIClient
from api.models.api_response import APIResponse

from api.schemas.products.products_response import ProductsResponse, ProductActionResponse


class ProductsClient:
    """
    Клиент для работы с products
    """

    def __init__(self, client: APIClient):
        self.client = client

    def get_all_products(self) -> APIResponse[ProductsResponse]:
        response = self.client.get("/productsList")
        return self.client.parse_response(response, ProductsResponse)

    def search_product(self, search_product: str) -> APIResponse[ProductsResponse]:
        response = self.client.post("/searchProduct", data={"search_product": search_product})
        return self.client.parse_response(response, ProductsResponse)

    def search_product_without_query(self) -> APIResponse[ProductActionResponse]:
        response = self.client.post("/searchProduct")
        return self.client.parse_response(response, ProductActionResponse)

    

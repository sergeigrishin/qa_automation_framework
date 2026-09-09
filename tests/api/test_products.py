from api.clients.products_client import ProductsClient
import pytest

@pytest.mark.positive
@pytest.mark.api
def test_get_all_products(products_client: ProductsClient):

    response = products_client.get_all_products()

    assert response.status_code == 200
    assert len(response.data.products) > 0


@pytest.mark.positive
@pytest.mark.api
def test_search_product(products_client: ProductsClient):
    response = products_client.search_product("top")

    assert response.status_code == 200
    assert len(response.data.products) > 0


@pytest.mark.negative
@pytest.mark.api
def test_search_product_without_query(products_client: ProductsClient):
    response = products_client.search_product_without_query()

    assert response.status_code == 200
    assert response.data["responseCode"] == 400


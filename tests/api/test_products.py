import pytest
from http import HTTPStatus
import allure

from api.clients.products_client import ProductsClient


@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.api
@allure.title("Получение списка всех продуктов")
@allure.description("Проверка успешного получения списка продуктов через API")
def test_get_all_products(products_client: ProductsClient):
    response = products_client.get_all_products()

    assert response.status_code == HTTPStatus.OK
    assert response.data.response_code == HTTPStatus.OK
    assert response.data

    assert all(product.id > 0 for product in response.data.products)
    assert all(product.name for product in response.data.products)
    assert all(product.brand for product in response.data.products)
    assert all(product.price.startswith("Rs. ") for product in response.data.products)
    assert all(product.category.category for product in response.data.products)
    assert all(product.category.usertype.usertype for product in response.data.products)


@pytest.mark.regression
@pytest.mark.flaky(reruns=1)
@pytest.mark.positive
@pytest.mark.api
def test_search_product(products_client: ProductsClient):
    response = products_client.search_product("top")

    assert response.data.response_code == HTTPStatus.OK

    product = next(
        (
            product
            for product in response.data.products
            if 'top' in product.name.lower()
        ),
        None
    )

    assert product is not None
    assert product.price
    assert product.brand


@pytest.mark.regression
@pytest.mark.negative
@pytest.mark.api
def test_search_product_without_query(products_client: ProductsClient):
    response = products_client.search_product_without_query()

    assert response.data.response_code == HTTPStatus.BAD_REQUEST
    assert response.data.message == "Bad request, search_product parameter is missing in POST request."

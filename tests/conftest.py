from httpx import Client
from playwright.sync_api import Page
from http import HTTPStatus
from api.clients.user_client import UserClient
from api.config.settings import Settings
from api.clients.products_client import ProductsClient
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from api.data.user import User
from api.clients.api_client import APIClient
import pytest


@pytest.fixture(scope="session", autouse=True)
def configure_playwright_selectors(playwright):
    playwright.selectors.set_test_id_attribute("data-qa")


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def user() -> User:
    return User.create_user()


@pytest.fixture
def registration_page(page: Page) -> RegistrationPage:
    return RegistrationPage(page)


@pytest.fixture
def settings() -> Settings:
    return Settings()


@pytest.fixture
def products_client(settings: Settings) -> ProductsClient:
    client = Client(base_url=settings.API_BASE_URL)
    public_client = APIClient(client)
    yield ProductsClient(public_client)
    client.close()


@pytest.fixture
def user_client(settings: Settings) -> UserClient:
    client = Client(base_url=settings.API_BASE_URL)
    public_client = APIClient(client)
    yield UserClient(public_client)
    client.close()


@pytest.fixture
def registered_user(user_client):
    user = User()

    response = user_client.create_account(user)
    assert response.data.response_code == HTTPStatus.CREATED

    original_email = user.email
    original_password = user.password

    yield user

    user_client.delete_account(
        email=original_email,
        password=original_password
    )


from multiprocessing.connection import Client
from httpx import Client
from playwright.sync_api import Page
import pytest

from api.clients.auth_client import AuthClient
from config.settings import Settings
from api.clients.products_client import ProductsClient
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from api.data.user import User
from api.clients.public_client import PublicAPIClient


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
    public_client = PublicAPIClient(client)
    yield ProductsClient(public_client)
    client.close()


@pytest.fixture
def auth_client(settings: Settings):
    client = Client(base_url=settings.API_BASE_URL)
    public_client = PublicAPIClient(client)
    yield AuthClient(public_client)
    client.close()

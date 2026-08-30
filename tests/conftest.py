from playwright.sync_api import Page
import pytest
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from tests.data.user_factory import UserFactory
from tests.data.user import User



@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def user() -> User:
    return UserFactory.create_user()


@pytest.fixture
def registration_page(page: Page) -> RegistrationPage:
    return RegistrationPage(page)


@pytest.fixture(scope="session", autouse=True)
def configure_playwright_selectors(playwright):
    playwright.selectors.set_test_id_attribute("data-qa")

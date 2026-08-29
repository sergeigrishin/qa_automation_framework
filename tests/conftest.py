from playwright.sync_api import Page
import pytest
from pages.login_page import LoginPage
from tests.data.user_factory import UserFactory
from tests.data.user_default import User


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def user() -> User:
    return UserFactory.create_user()

from playwright.sync_api import expect
from tests.data.user import User


def test_login(login_page):
    default_user = User()

    login_page.open()
    login_page.login(email=default_user.email, password=default_user.password)

    user_locator = login_page.header.get_logged_in_user_locator(default_user.name)
    expect(user_locator).to_be_visible()

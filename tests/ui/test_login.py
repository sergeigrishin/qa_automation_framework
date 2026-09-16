from playwright.sync_api import expect
from api.data.user import User
import pytest


@pytest.mark.ui
@pytest.mark.negative
def test_login_invalid_user(login_page):
    default_user = User()

    login_page.open()
    login_page.login(email=default_user.email, password=default_user.password)

    expect(login_page.login_error).to_be_visible()
    expect(login_page.login_error).to_have_text('Your email or password is incorrect!')

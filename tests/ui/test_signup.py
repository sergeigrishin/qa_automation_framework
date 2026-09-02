from playwright.sync_api import expect
import pytest
from tests.data.user_default import UserDefault

@pytest.mark.negative
def test_signup(login_page):
    user = UserDefault()

    login_page.open()
    login_page.start_signup(name=user.name, email=user.email)
    expect(login_page.existing_email_error).to_be_visible()
    expect(login_page.existing_email_error).to_have_text("Email Address already exist!")
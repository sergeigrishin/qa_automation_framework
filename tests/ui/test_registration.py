from tests.data.user import User
from playwright.sync_api import expect
import pytest


@pytest.mark.positive
def test_registration(login_page, registration_page):
    user_default = User()

    login_page.open()
    login_page.start_signup(user_default.name, user_default.email)

    registration_form_title = (
        registration_page.get_registration_form_title()
    )

    expect(registration_form_title).to_be_visible()

    expect(registration_form_title).to_have_text(
        "Enter Account Information"
    )

    expect(registration_page.name_input).to_have_value(user_default.name)
    expect(registration_page.email_input).to_have_value(user_default.email)

    registration_page.select_mr_title()

    registration_page.fill_password_information(user_default.password)
    registration_page.select_date_of_birth(2, 4, 2000)
    registration_page.subscribe_to_newsletter()
    registration_page.subscribe_to_partner_offers()

    registration_page.fill_address_information(
        first_name=user_default.first_name,
        last_name=user_default.last_name,
        company='AO LLI',
        address=user_default.address,
        address_2=user_default.address
    )
    registration_page.select_country('Canada')
    registration_page.fill_location_information(state='Canada', city='Toronto', zipcode='60456')
    registration_page.fill_contact_information('457392')
    registration_page.click_button_create_account()

    expect(registration_page.page).to_have_url('https://automationexercise.com/account_created')
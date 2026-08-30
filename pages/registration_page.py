from pages.base_page import BasePage
from playwright.sync_api import Page


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Registration form
        self.registration_form_title = page.get_by_text(
            "Enter Account Information"
        )
        # Title
        self.mr_title_radiobutton = page.locator("//input[@id='id_gender1']")
        self.mrs_title_radiobutton = page.locator("//input[@id='id_gender2']")

        # Account_info
        self.name_input = page.get_by_test_id('name')
        self.email_input = page.get_by_test_id('email')
        self.password_input = page.get_by_test_id('password')

        # Birth
        self.day_date_of_birth = page.get_by_test_id('days')
        self.month_date_of_birth = page.get_by_test_id('months')
        self.year_date_of_birth = page.get_by_test_id('years')

        # Checkbox info
        self.newsletter_checkbox = page.locator("//div//input[@id='newsletter']")
        self.offers_from_our_partners_checkbox = page.locator("//div//input[@id='optin']")

        # Address
        self.first_name_input = page.get_by_test_id('first_name')
        self.last_name_input = page.get_by_test_id('last_name')
        self.company_input = page.get_by_test_id('company')
        self.address_input = page.get_by_test_id('address')
        self.address_2_input = page.get_by_test_id('address2')

        # Select country
        self.country_select = page.get_by_test_id("country")
        self.state_input = page.get_by_test_id('state')
        self.city_input = page.get_by_test_id('city')
        self.zipcode_input = page.get_by_test_id('zipcode')

        # Mobile number
        self.mobile_number_input = page.get_by_test_id('mobile_number')

        # Create account button
        self.create_account_button = page.get_by_test_id('create-account')

        # Subscription
        self.subscription_email_input = page.locator("//div//input[@id='susbscribe_email']")
        self.subscription_email_button = page.locator("//div//input[@id='subscribe']")

    def get_registration_form_title(self):
        return self.registration_form_title

    def select_mr_title(self):
        self.mr_title_radiobutton.check()

    def select_mrs_title(self):
        self.mrs_title_radiobutton.check()

    def subscribe_to_newsletter(self):
        self.newsletter_checkbox.check()

    def subscribe_to_partner_offers(self):
        self.offers_from_our_partners_checkbox.check()

    def fill_password_information(self, password: str):
        self.password_input.fill(password)

    def select_date_of_birth(self, day: int, month: int, year: int):
        self.day_date_of_birth.select_option(value=str(day))
        self.month_date_of_birth.select_option(value=str(month))
        self.year_date_of_birth.select_option(value=str(year))

    def fill_address_information(self, first_name: str, last_name: str, company: str, address: str, address_2: str):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.company_input.fill(company)
        self.address_input.fill(address)
        self.address_2_input.fill(address_2)

    def select_country(self, country: str):
        self.country_select.select_option(label=country)

    def fill_location_information(
            self,
            state: str,
            city: str,
            zipcode: str
    ):
        self.state_input.fill(state)
        self.city_input.fill(city)
        self.zipcode_input.fill(zipcode)

    def fill_contact_information(self, number: str):
        self.mobile_number_input.fill(number)

    def click_button_create_account(self):
        self.create_account_button.click()

    def create_subscription(self, email: str):
        self.subscription_email_input.fill(email)
        self.subscription_email_button.click()

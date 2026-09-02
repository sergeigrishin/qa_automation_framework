from playwright.sync_api import Page
from components.header import HeaderComponent
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = self.page.get_by_test_id("login-email")
        self.password_input = self.page.get_by_test_id('login-password')
        self.login_button = self.page.get_by_test_id('login-button')

        self.name_user_signup_input = self.page.locator("//div//input[@data-qa='signup-name']")
        self.email_user_signup_input = self.page.get_by_test_id('signup-email')
        self.signup_user_button = self.page.get_by_test_id('signup-button')
        self.signup_existing_email_error = page.get_by_text(
            "Email Address already exist!"
        )

        self.header = HeaderComponent(page)

    def open(self):
        self.visit('https://www.automationexercise.com/login')

    def fill_login_form(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)

    def click_login_button(self):
        self.login_button.click()

    def login(self, email: str, password: str):
        self.fill_login_form(email, password)
        self.click_login_button()

    def start_signup(self, name: str, email: str):
        self.name_user_signup_input.fill(name)
        self.email_user_signup_input.fill(email)
        self.signup_user_button.click()

    def get_existing_email_error(self):
        return self.existing_email_error

from playwright.sync_api import Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = self.page.locator("input[data-qa='login-email']")
        self.password_input = self.page.locator("input[data-qa='login-password']")
        self.login_button = self.page.locator("button[data-qa='login-button']")

    def open(self):
        self.visit('https://www.automationexercise.com/login')

    def fill_login_form(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)

    def click_login_button(self):
        self.login_button.click()

    def login(self, email: str, password: str):
        self.fill_login_form(email, password)
        self.login_button.click()

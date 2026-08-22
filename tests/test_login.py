import time

from playwright.sync_api import Page, sync_playwright


def test_login(page: Page):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://automationexercise.com/signup")

        email_address = page.locator("[data-qa='login-email']")
        email_address.fill('user_new_user@gmail.com')

        user_password = page.locator("[data-qa='login-password']")
        user_password.fill('123Qwerty!')

        login_button = page.locator("[data-qa='login-button']")
        login_button.click()
        time.sleep(5)


from playwright.sync_api import Page


class HeaderComponent:
    def __init__(self, page: Page):
        self.page = page

    def get_logged_in_user_locator(self, username:str):
        return self.page.get_by_text(f"Logged in as {username}")


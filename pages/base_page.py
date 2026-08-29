from playwright.sync_api import Page
from components.header import HeaderComponent


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.header = HeaderComponent(page)

    def visit(self, url: str):
        self.page.goto(url, wait_until='load')

    def reload(self):
        self.page.reload(wait_until='domcontentloaded')


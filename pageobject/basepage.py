from playwright.sync_api import Page


class BasePage(object):
    def __init__(self, page: Page):
        self.page = page
        page.goto("https://cn.bing.com")
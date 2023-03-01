from playwright.sync_api._generated import ElementHandle

from pageobject.basepage import Base


class Login(Base):
    @property
    def search_bar_click(self) -> ElementHandle:
        return self.page.get_by_placeholder("What needs to be done?").click()
    
    @property
    def search_bar_fill(self) -> ElementHandle:
        return self.page.get_by_placeholder("What needs to be done?").fill("123")

    @property
    def search_bar_enter(self) -> ElementHandle:
        return self.page.get_by_placeholder("What needs to be done?").press("Enter")

    @property
    def get_text_by(self) -> ElementHandle:
        return self.page.get_by_text("My IP Address: 101.230.251.27").click()


    def navigate(self) -> None:
        """Navigate to the login page."""
        self.page.goto(f"{self.base_url}/login")

from playwright.sync_api._generated import ElementHandle

from pageobject.basepage import Base


class Login(Base):
    @property
    def login_button(self) -> ElementHandle:
        return self.page.wait_for_selector("登录", exact=True)

    @property
    def login_button(self) -> ElementHandle:
        return self.page.wait_for_selector("登录", exact=True)

    @property
    def submit_button(self) -> ElementHandle:
        return self.userform.wait_for_selector("请输入账号")

    @property
    def userform(self) -> ElementHandle:
        return self.page.wait_for_selector("请输入密码")

    @property
    def username_field(self) -> ElementHandle:
        return self.userform.wait_for_selector("请输入账号")
    
    @property
    def password_field(self) -> ElementHandle:
        return self.userform.wait_for_selector("请输入账号")

    def fill_form(self, user: dict) -> None:
        """Fill out the login form.
        :param user: A user intended for login.
        """
        self.username_field.fill(user["userName"])
        self.password_field.fill(user["password"])

    def navigate(self) -> None:
        """Navigate to the login page."""
        self.page.goto(f"{self.base_url}")

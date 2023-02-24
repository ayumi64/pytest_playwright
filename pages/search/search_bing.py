from playwright.sync_api._generated import ElementHandle

from pages.basepage import BasePage

# 方法1 元素分离
search_input = "input[name=\"q\"]"
search_button = "[aria-label=\"搜索网页\"] svg"

class BingSearch(BasePage):
    
    # 方法1 操作元素
    def search_bar_click1(self) -> ElementHandle:
        return self.page.click(search_input)

    def search_bar_input1(self) -> ElementHandle:
        return self.page.fill(search_input, "playwright")

    def search_button1(self) -> ElementHandle:
        return self.page.click(search_button)

    # 方法2 元素和操作绑定
    def search_bar_click2(self) -> ElementHandle:
        return self.page.click("input[name=\"q\"]")

    def search_bar_input2(self, text) -> ElementHandle:
        self.page.fill("input[name=\"q\"]", text)

    def search_button2(self) -> ElementHandle:
        return self.page.click(search_button)
    
    # 方法3 操作绑定
    def search3(self, text) -> ElementHandle:
        self.page.click(search_button)
        self.page.fill("input[name=\"q\"]", text)
        self.page.click("[aria-label=\"搜索网页\"] svg")
    
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
        self.password_field.fill(user["passWord"])

    def navigate(self) -> None:
        """Navigate to the login page."""
        self.page.goto(f"{self.base_url}")

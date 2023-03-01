import pytest
from playwright.async_api import async_playwright
from playwright.async_api._generated import ElementHandle
from pytest import fixture
import time
from pageobject.login.login_demo import Login

base_url: str = "https://cn.bing.com"

timenow = time.time()

@pytest.mark.asyncio
class TestBase:
    async def test_visit_page_title(self) -> None:
        """Test that the Elements page can be navigated to.

        :param page: A Playwright browser page.
        """
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch()
            page = await browser.new_page()
            await page.goto(f"{base_url}")
            header_text: str = await page.title()
            page.screenshot(path=f'example-{timenow}.png')
            assert "What's my User Agent?" == header_text
            browser.close()

    async def test_input(self) -> None:
        """Test that the Elements container may be collapsed by a user.

        :param page: A Playwright browser page.
        """
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch()
            page = await browser.new_page()

            page.get_by_placeholder("What needs to be done?").fill("123")
            page.get_by_placeholder("What needs to be done?").press("Enter")
            todo_title = page.get_by_text("todo-title")
            
            assert "123" == todo_title

    async def test_wait_for_selector(self) -> None:
            
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch(headless=False)
            page = await browser.new_page()
            await page.goto(f"{base_url}")

            login_page = Login.get_text_by
            
            header_text: str = await page.title()
            page.screenshot(path='screenshot/xxx.png')

            print(header_text)
            
            assert "What's my User Agent?" == header_text
            browser.close()
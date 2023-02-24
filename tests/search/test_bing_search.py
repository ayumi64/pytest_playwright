import pytest
from playwright.async_api import async_playwright
from playwright.async_api._generated import ElementHandle
from pytest import fixture
import time
from pages.search.search_bing import BingSearch
from playwright.sync_api import Page

base_url: str = "https://cn.bing.com"

timenow = time.time()

@pytest.mark.asyncio
class TestBase:
    
    def test0_search_playwright(self, page: Page) -> None:
        
            new_search: BingSearch = BingSearch(page)
            new_search.search_bar_click1()
            new_search.search_bar_input1()
            new_search.search_button1()
            header_text: str = page.title()
            
            print(header_text)
            page.screenshot(path=f'example-{timenow}.png')
            assert "playwright" in header_text            
    
    
    def test1_search_playwright(self, page: Page) -> None:
        """
        Test that the Elements page can be navigated to.
        :param page: A Playwright browser page.
        """

        new_search = BingSearch(page)
        new_search.search_bar_click1()
        new_search.search_bar_input1()
        new_search.search_button1()
        header_text: str = page.title()
        
        print(header_text)
        page.screenshot(path=f'example-{timenow}.png')
        assert "playwright" in header_text

            
    def test2_search_playwright(self, page: Page) -> None:
        """
        Test that the Elements page can be navigated to.
        :param page: A Playwright browser page.
        """

        new_search = BingSearch(page)
        new_search.search_bar_click2()
        new_search.search_bar_input2("selenium")
        new_search.search_button2()
        header_text: str = page.title()
        print(header_text)
        assert "selenium" in header_text

            
    def test3_search_playwright(self, page: Page) -> None:
        """
        Test that the Elements page can be navigated to.
        :param page: A Playwright browser page.
        """

        new_search = BingSearch(page)
        new_search.search3(text="chatGPT")

        header_text: str = page.title()
        print(header_text)
        page.screenshot(path=f'example-{timenow}.png')
        assert "chatGPT" in header_text

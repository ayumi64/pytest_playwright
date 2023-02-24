from playwright.sync_api import sync_playwright
import pytest

async def handle(route):
    json = { message: {"test_breed": []}}
    route.fulfill(json=json)
    
with sync_playwright() as p:
        browser_type = p.chromium
        browser = browser_type.launch(headless=False)
        page = browser.new_page()

page.route("https://dog.ceo/api/breeds/list/all", handle)

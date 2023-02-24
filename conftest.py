from typing import Union

import pytest
from pytest import fixture
from playwright.sync_api import sync_playwright


# @pytest.fixture(scope='session', autouse=True)
# def drivers(request):
    
#     global page
    
#     with sync_playwright() as p:
        
#         for browser_type in [p.chromium]:
#             browser = browser_type.launch(headless=False)
#             page = browser.new_page()
#             page.goto("https://cn.bing.com")
#             page.screenshot(path=f'screenshot/example-{browser_type.name}.png')

#     # def fn():
#     #     page.close()

#     # request.addfinalizer(fn)
#     return page
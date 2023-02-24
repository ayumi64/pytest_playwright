import pytest

def test_example_is_working(page):
    page.goto("https://example.com")
    page.waitForSelector("text=Example Domain")
    page.click("text=More information")


@pytest.mark.skip_browser("chrome")
def test_visit_example(page):
    page.goto("https://example.com")


@pytest.mark.only_browser("chromium")
def test_visit_example(page):
    page.goto("https://example.com")

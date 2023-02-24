import pytest


@pytest.mark.only_browser("chromium")
def test_visit_example(page):
    page.goto("https://example.com")

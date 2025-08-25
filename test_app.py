import pytest
from playwright.sync_api import sync_playwright

def test_homepage_shows_title():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:5000")
        assert "Book Review Hub" in page.content()
        browser.close()
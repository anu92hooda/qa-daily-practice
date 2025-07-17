
from playwright.sync_api import sync_playwright ,Page, expect
from pytest_playwright.pytest_playwright import browser

def test_mobile_emulation():

    with sync_playwright() as p:

        iphone= p.devices['iPhone 11']

        browser= p.chromium.launch(headless=False)
        context= browser.new_context(
            **iphone
        )

        page= context.new_page()
        page.goto("https://playwright.dev/")

        page.wait_for_timeout(3000)
        page.screenshot(path= "screenshots/day23.png")

        context.close()
        browser.close()

def test_custom_mobile_emulation():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context= browser.new_context(viewport={"width": 390, "height": 844},
                                     user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)...",
                                     device_scale_factor=3,
                                     is_mobile=True,
                                     has_touch=True,
                                     )

        page= context.new_page()
        page.goto("https://www.wikipedia.org")
        page.fill("input[name='search']", "Cristiano Ronaldo")
        page.get_by_role("button", name="Search").click()
        page.wait_for_timeout(1000)
        page.screenshot(path= "screenshots/day23ronaldo.png")

        context.close()
        browser.close()






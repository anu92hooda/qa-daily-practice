from playwright.sync_api import sync_playwright , expect, Page
from pytest_playwright.pytest_playwright import browser


def test_cross_browser():
    with sync_playwright() as p:

        iphone= p.devices['iPhone 11']
        browsers = {
            "chromium": p.chromium,
            "webkit": p.webkit
        }

        for name, engine in browsers.items():
            print(f"\n--- Running on {name}---")
            browser= engine.launch(headless=False)

            if name == "webkit":
                context = browser.new_context(**iphone)
            else:
                context = browser.new_context()

            page= context.new_page()

            page.goto("https://www.wikipedia.org")
            page.fill("input[name='search']", "Cristiano Ronaldo")
            page.get_by_role("button", name="Search").click()
            page.wait_for_timeout(1000)

            page.screenshot(path=f"screenshots/day23{name}.png")

            context.close()
            browser.close()




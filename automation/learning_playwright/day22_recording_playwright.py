import os

from playwright.sync_api import sync_playwright
from playwright.sync_api import expect , Page
from pytest_playwright.pytest_playwright import playwright, context


def test_day22_third():

    os.makedirs("videos", exist_ok=True)

    with sync_playwright() as p:
        browser= p.chromium.launch(headless=False)
        context= browser.new_context(
            record_video_dir="videos/" ,
            record_video_size={"width":1280 , "height": 720}
        )

        page= context.new_page()
        page.goto("https://playwright.dev/")
        page.click("text=Get Started")

        page.wait_for_timeout(3000)
        context.close()
        browser.close()

        print("video saved in videos")

test_day22_third()
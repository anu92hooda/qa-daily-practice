
from playwright.sync_api import sync_playwright

def run_test():
    with sync_playwright() as p:

        browser= p.chromium.launch(headless=False)

        # Create a new isolated context (like an incognito user session)
        context= browser.new_context()

        #Open new tab in that browser
        page= context.new_page()

        #Navigate to the website
        page.goto("https://example.com")

        #click a link that contains visible text
        page.click("text=More information")

        #close the browser
        browser.close()

#run_test()

def run_test2():

    with sync_playwright() as p:
        browser= p.chromium.launch(headless=False)
        context= browser.new_context()
        page=context.new_page()
        page.goto("https://the-internet.herokuapp.com/login", timeout=1000)
        page.fill("#username", "tomsmith")
        page.fill("#password", "SuperSecretPassword!")

        page.click("button[type= 'submit']")

        page.wait_for_selector(".flash.success")


        success_message= page.text_content(".flash.success")
        print("login success", success_message.strip())

        assert "You logged into a secure area!" in success_message

        browser.close()

run_test2()



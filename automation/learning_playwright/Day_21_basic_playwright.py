from playwright.sync_api import sync_playwright
from pytest_playwright.pytest_playwright import playwright
from playwright.sync_api import expect
from playwright.sync_api import Page


def test_day21_first():

    with sync_playwright() as p:
        browser= p.chromium.launch(headless=False)
        page= browser.new_page()

        page.goto("https://playwright.dev/")

        page.screenshot(path="basic_test.png")

        print(page.title())

        assert  "Playwright" in page.title()

        browser.close()

# run the code inside only if script is not imported elsewhere
#if __name__ == '__main__':
   # test_day21_first()

def test_day21_second():

    with sync_playwright() as p:
        browser= p.chromium.launch(headless=False)
        page= browser.new_page()
        page.goto("https://playwright.dev/python/docs/intro")

        #page.click("button[title='Search']")
        page.get_by_role("button", name="Search").click()

        page.fill("input[type='search']", "screenshot")
        #page.get_by_role("combobox").fill("screenshot")

        page.wait_for_timeout(2000)
        page.screenshot(path= "test_day1_second.png")

        browser.close()

#test_day21_second()

def test_day21_third():

    with sync_playwright() as p:
        browser= p.chromium.launch(headless=False)
        page= browser.new_page()

        page.goto("https://demoqa.com/text-box")

        page.get_by_placeholder("Full Name").fill("Anu QA")
        page.get_by_placeholder("name@example.com").fill("anu@gmail.com")
        page.locator("#currentAddress").fill("123 QA")
        page.locator("#permanentAddress").fill("456 Testing Ave")

        page.get_by_role("button", name="Submit").click()

        page.wait_for_timeout(2000)

        page.screenshot(path="test_21_third.png")

        name_out= page.locator("#name")
        expect(name_out).to_have_text("Name:Anu QA")

        email_out= page.locator("#email")
        expect(email_out).to_have_text("Email:anu@gmail.com")

        add_out= page.locator("p#currentAddress")
        expect(add_out).to_contain_text("Current Address :123 QA")

        add_per_out= page.locator("p#permanentAddress")
        expect(add_per_out).to_contain_text("Permananet Address :456 Testing Ave")

        browser.close()

test_day21_third()















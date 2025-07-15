
from  playwright.sync_api import sync_playwright
from automation.learning_playwright_POM.pages.text_box_page import TextBoxPage


def test_text_box_form():

    with sync_playwright() as p:
        browser= p.chromium.launch(headless=False)
        page= browser.new_page()

        page.goto("https://demoqa.com/text-box")

        #creating object
        text_box= TextBoxPage(page)

        #using methods
        text_box.fill_form(
            name="Anu QA",
            email="anu@gmail.com",
            current="514 street",
            permanent="122 street"
         )

        text_box.submit_form()

        text_box.assert_result("Anu QA","anu@gmail.com", "514 street", "122 street" )
        print("✅ Test completed successfully!")

        browser.close()

test_text_box_form()
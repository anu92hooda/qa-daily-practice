from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
from playwright.sync_api import Page

class TextBoxPage:

    def __init__(self, page:Page):
        self.page= page

        #locators
        self.full_name_input= page.get_by_placeholder("Full Name")
        self.email_input= page.get_by_placeholder("name@example.com")
        self.current_address_input= page.locator("#currentAddress")
        self.permanent_address= page.locator("#permanentAddress")
        self.submit_button= page.get_by_role("button", name="Submit")

        self.name_out = page.locator("#name")
        self.email_out = page.locator("#email")
        self.add_out = page.locator("p#currentAddress")
        self.add_per_out = page.locator("p#permanentAddress")

    def fill_form(self , name: str , email: str , current: str , permanent: str ):
        self.full_name_input.fill(name)
        self.email_input.fill(email)
        self.current_address_input.fill(current)
        self.permanent_address.fill(permanent)

    def submit_form(self):
        self.submit_button.click()

    def assert_result(self, name: str , email: str , current: str , permanent: str):
        expect(self.name_out).to_have_text(f"Name:{name}")
        expect(self.email_out).to_have_text(f"Email:{email}")
        expect(self.add_out).to_contain_text(f"Current Address :{current}")
        expect(self.add_per_out).to_contain_text(f"Permananet Address :{permanent}")



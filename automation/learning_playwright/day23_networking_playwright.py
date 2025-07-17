from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect, Request,Route

def handle_route(route: Route, request: Request):

    if "jsonplaceholder.typicode.com/todos/1" in request.url:
        route.fulfill(
            status=200,
            content_type="application/json",
            body= '{"userId": 1, "id": 1, "title": "Mocked Title", "completed": true}'

                   )
    else:

        route.continue_()


def test_network_mocking():

    with sync_playwright() as p:
        browser= p.chromium.launch(headless=False)
        context= browser.new_context()
        page= context.new_page()

        page.route("**/todos/1", handle_route)
        page.goto("https://jsonplaceholder.typicode.com/todos/1")

        print("API mocked")

        context.close()
        browser.close()






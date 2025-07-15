import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException , TimeoutException , ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def driver():
    driver= webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.flaky(reruns=2, reruns_delay=1)
def test_action_pro(driver):

    driver.get("https://demoqa.com/menu")
    wait = WebDriverWait(driver, 10)
    actions= ActionChains(driver)

    main_menu = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Main Item 2']")))
    actions.move_to_element(main_menu).perform()

    sub_menu = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='SUB SUB LIST »']")))
    actions.move_to_element(sub_menu).perform()



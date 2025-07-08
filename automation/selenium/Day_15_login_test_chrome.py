from zipfile import error
import os
from datetime import  datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
import time

def test_1_pos():

    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.maximize_window()

    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    button = driver.find_element(By.XPATH, "//button[@id='submit']")

    try:

        wait= WebDriverWait(driver, 10)
        username.send_keys("student")
        password.send_keys("Password123")
        button.click()
        #time.sleep(2)

        wait.until(EC.url_to_be("https://practicetestautomation.com/logged-in-successfully/"))

        expected_url= "https://practicetestautomation.com/logged-in-successfully/"
        if driver.current_url == expected_url:
            print("login passed")
        else:
            print("login failed")

    except Exception as e:
        print(f"Test failed:{e}")
        os.makedirs("selenium/screenshots", exist_ok=True)
        timestamp= datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        driver.save_screenshot(f"selenium/screenshots/failure_{timestamp}.png")
        print(f"Screenshot saved : failure_{timestamp}.png")

    finally:
        driver.quit()

test_1_pos()


def test_1_neg():

    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.maximize_window()

    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    button = driver.find_element(By.XPATH, "//button[@id='submit']")

    try:
        wait= WebDriverWait(driver, 10)
        username.send_keys("wronguser")
        password.send_keys("wrongpass")
        button.click()
        time.sleep(2)

        error_message= driver.find_element(By.XPATH, "//div[@id='error']")
        #error_message= wait.until(EC.visibility_of_element_located(By.ID, "error"))
        expected_message= "Your username is invalid!"
        actual_message= error_message.text

        if expected_message in actual_message:
            print("Negative login test passed: error message displayed.")
        else:
            print("negative test case failed")

    finally:
        driver.quit()

#test_1_neg()








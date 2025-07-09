from selenium import webdriver
from selenium.webdriver.common.by import By
from applitools.selenium import Eyes
import os

eyes = Eyes()
eyes.api_key = "SmhHUqAKA106SKYddfy4310owogwEclbynQ5VkXDfeBkU110"

driver = webdriver.Chrome()

try:
    eyes.open(driver, "Demo App", "Login Visual Test", {'width': 800, 'height': 600})
    driver.get("https://demo.applitools.com")
    eyes.check_window("Login Page")

    driver.find_element(By.ID, "username").send_keys("user")
    driver.find_element(By.ID, "password").send_keys("password")
    driver.find_element(By.ID, "log-in").click()

    eyes.check_window("Dashboard Page")
    eyes.close()

finally:
    driver.quit()
    eyes.abort_if_not_closed()

from marshmallow.utils import timestamp
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import  os
from datetime import  datetime

try:
    driver= webdriver.Chrome()
    #driver.implicitly_wait(5)
    driver.get("https://www.saucedemo.com/")

    #driver.find_element(By.ID, "user-name").send_keys("standard_user")
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID,"user-name1"))).send_keys("standard_user")
    #driver.find_element(By.ID,"password").send_keys("secret_sauce")
    WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.ID,"password"))).send_keys("secret_sauce")
    #driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"login-button"))).click()
    url_name= driver.find_element(By.CLASS_NAME,"title").text
    print(f"you login {url_name}")

except Exception as e:

    os.makedirs("screenshots", exist_ok=True)
    timestamp= datetime.now().strftime("%Y%m%d_%H%M%S")
    ss_path=f"screenshots/failure_{timestamp}.png"

    driver.save_screenshot(ss_path)
    print(f"there is an error {e}")
    print(f" Screenshot save at: {ss_path}")

finally:
    driver.quit()

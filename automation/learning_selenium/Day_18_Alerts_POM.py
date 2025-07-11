from imghdr import tests
from time import sleep

from marshmallow.utils import timestamp
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver.support.ui import Select
import os
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException



# Driver

def dayalerts():
    try:
        driver= webdriver.Chrome()
        driver.maximize_window()
        sleep(2)

        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
        alerts= driver.switch_to.alert
        alerttext1= alerts.text
        print(alerttext1)
        alerts.accept()

        driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
        #WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Click for JS Confirm']"))).click()
        alerts= driver.switch_to.alert
        alerttest2= alerts.text
        print(alerttest2)
        alerts.dismiss()

        driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
        alerts= driver.switch_to.alert
        alerttest3 = alerts.text
        alerts.send_keys("Hello")
        alerts.accept()



    except Exception as e:

        os.makedirs("screenshots", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        ss_path = f"screenshots/failure_{timestamp}.png"
        driver.save_screenshot(ss_path)
        print(f"there is an error{e}")
        print(f" Screenshot save at: {ss_path}")


    finally:
        driver.quit()

#dayalerts()

def daydrop():
    try:
        driver= webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(4)

        driver.get("https://the-internet.herokuapp.com/dropdown")
        #dropdown= Select(driver.find_element(By.ID, "dropdown"))
        dropdown= Select(WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID,"dropdown" ))))

        dropdown.select_by_index(0)
        dropdown.select_by_value("2")
        dropdown.select_by_visible_text("Option 1")
        selecteddrop = dropdown.first_selected_option.text
        print("selected")


    except NoSuchElementException as ne:
        print(f"there is an error{ne}")

    except Exception as e:

        os.makedirs("screenshots", exist_ok=True)
        timestamp= datetime.now().strftime("%Y%m%d_%H%M%S")
        ss_path= f"screenshots/failure_{timestamp}.png"
        driver.save_screenshot(ss_path)

        print(f"there is an error{e}")
        print(f" Screenshot save at: {ss_path}")

    finally:
        driver.quit()

#daydrop()

def daywindow():
    try:

        driver= webdriver.Chrome()
        driver.get("https://the-internet.herokuapp.com/windows")
        original_window= driver.current_window_handle
        print(original_window)

        # next tab
        driver.find_element(By.LINK_TEXT, "Click Here").click()
        handles= driver.window_handles
        print(handles)
        #handles will have two id , original and new open one

        for handle in handles:
             if handle != original_window:
                 driver.switch_to.window(handle)
                 break

        print("new tab title", driver.title)
        driver.close()

        driver.switch_to.window(original_window)
        print("back to original", driver.title)

    except NoSuchElementException as ne:
        print("Error Occured" , ne)

    except Exception as e:

        os.makedirs("screenshots",exist_ok=True)
        timestamp= datetime.now().strftime("%Y%m%d_%H%M%S")
        ss_path= f"screenshots/failure_{timestamp}.png"

        driver.save_screenshot(ss_path)
        print(f"there is an error{e}")
        print(f" Screenshot save at: {ss_path}")


    finally:
        print("Everything okay, Testing completed ")
        driver.quit()

#daywindow()

def dayiframe():
    driver= webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://demo.automationtesting.in/Frames.html")
    driver.switch_to.frame(driver.find_element(By.ID,"singleframe"))
    textbox= driver.find_element(By.XPATH,"//input[@type='text']")
    textbox.send_keys("Hello Iframe!")
    driver.switch_to.default_content()


    driver.find_element(By.XPATH , "//a[text()='Iframe with in an Iframe']").click()

    print("iframe")

    driver.quit()

dayiframe()






import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException , TimeoutException , ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait

def testhower():

    try:
        driver= webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(1)

        actions= ActionChains(driver)
        wait= WebDriverWait(driver, 10)

        driver.get("https://demoqa.com/menu/")

        #driver.find_element(By.XPATH, "//a[text()='Main Item 2']")
        main_menu= wait.until(EC.visibility_of_element_located((By.XPATH,"//a[text()='Main Item 2']" )))
        actions.move_to_element(main_menu).perform()

        sub_menu= wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='SUB SUB LIST »']")))
        actions.move_to_element(sub_menu).perform()

    except TimeoutException as ti:
        print(ti)

    finally:
        driver.quit()

def test_drop():
    try:
        driver= webdriver.Chrome()
        driver.maximize_window()

        wait= WebDriverWait(driver, 10)
        actions= ActionChains(driver)

        driver.get("https://demoqa.com/droppable")

        source= wait.until(EC.visibility_of_element_located((By.ID, "draggable")))
        target= wait.until(EC.visibility_of_element_located((By.ID,"droppable")))

        #actions.drag_and_drop(source,target).perform()
        #time.sleep(2)

        actions.click_and_hold(source).pause(0.5)
        actions.move_to_element(target).pause(0.5)
        actions.release().perform()

        time.sleep(2)
        dropped= target.text
        assert "Dropped!" in dropped, "Drop action failed — text not updated"

        print("sucessfully droped ")

    except TimeoutException as e:
        print(e)


    finally:
        driver.quit()

test_drop()
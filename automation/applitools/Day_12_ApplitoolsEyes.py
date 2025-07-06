import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from applitools.selenium import Eyes
from applitools.common import  MatchLevel

# setup driver
driver= webdriver.Chrome()
driver.get("https://www.bing.com")
driver.maximize_window()

#Search for 'appitools'
search_Box= driver.find_element(By.NAME, "q")
search_Box.send_keys("applitools")
search_Box.send_keys(Keys.RETURN)
time.sleep(2)

#Accept cookies if present
try:
    driver.find_element(By.ID, "L2AGLb").click()  # Cookie popup

except:
    pass


#Initilize Eyes
eyes = Eyes()
eyes.api_key = "SmhHUqAKA106SKYddfy4310owogwEclbynQ5VkXDfeBkU110"
eyes.force_full_page_screenshot = True
eyes.match_level=MatchLevel.LAYOUT

try:
    eyes.open(driver, "Bing App", "Bing search Appitools + Functional Test)
    eyes.check_window("Full search result page")

    search_Box=driver.find_element(By.NAME, "q")
    eyes.check_region(search_Box , "Search Box only")

    eyes.close()

finally:
    eyes.abort_if_not_closed()
    driver.quit()


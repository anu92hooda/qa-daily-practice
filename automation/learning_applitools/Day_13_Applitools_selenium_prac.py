
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from applitools.selenium import Eyes, Target, BatchInfo
import time
from dotenv import load_dotenv
import os

#load .env file
load_dotenv()

# chrome driver setup
driver= webdriver.Chrome()
driver.get("https://www.bing.com")
driver.maximize_window()

# Initilize Eyes
eyes = Eyes()
eyes.api_key = os.getenv("APPLITOOLS_API_KEY")
eyes.batch= BatchInfo("Bing visual Batch")

try:
    eyes.open(driver, "Bing", "Applitools+Functional Testing")
    eyes.check("Home Page",Target.window().fully() )

    box= driver.find_element(By.NAME,'q')
    box.send_keys("AI QA Study roadmap")
    box.send_keys(Keys.RETURN)
    time.sleep(2)

    eyes.check("Search Results" ,Target.window().fully())

    eyes.close()



finally:
    driver.quit()
    eyes.abort_if_not_closed()








import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver_path = "E:/Dowmnload/Driver/chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
url = "https://selenium-python.readthedocs.io/"
driver.get(url)
time.sleep(10)

# Take ScreenShots
driver.save_screenshot("E:/Github_New/Web_Scraping/Selenium/ScreenShots/3_take_ScreenShots1.png")
time.sleep(4)

# Take ScreenShots any particular element
driver.find_element(By.XPATH, """/html/body/div[1]/div[2]/div/p/a/img""").screenshot("E:/Github_New/Web_Scraping/Selenium/ScreenShots/3_take_ScreenShots2.png")
time.sleep(4)
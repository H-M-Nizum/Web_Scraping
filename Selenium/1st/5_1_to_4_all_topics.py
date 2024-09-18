import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the WebDriver.
driver_path = 'E:/Dowmnload/Driver/chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

url = "https://www.google.com/"
driver.get(url) # Open this url in chrome web browzer
time.sleep(5)

search = driver.find_element(By.XPATH, """/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea""")
search.send_keys("House of the dragon")
search.send_keys(Keys.ENTER)
time.sleep(10)

# Click IMDb link
driver.find_element(By.XPATH, """/html/body/div[3]/div/div[13]/div[4]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div[2]/div/div/div/div/div/div[1]/div/div/span/a/h3""").click()
time.sleep(4)
driver.save_screenshot("E:/Github_New/Web_Scraping/Selenium/ScreenShots/5_Hous_of_the_Dragon.png")
time.sleep(10)
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
time.sleep(10)

# Find and catch search bar
search = driver.find_element(By.XPATH, """/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea""")
search.send_keys("Python Programming") # send text for search
search.send_keys(Keys.ENTER) # Press Enter button
time.sleep(10)

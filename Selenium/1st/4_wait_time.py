import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver
driver_path = 'E:/Dowmnload/Driver/chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Open the URL in Chrome browser
url = "https://www.google.com/"
driver.get(url)

# Wait for the search bar to become visible
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea"))
)

# Send text for search
element.send_keys("Python Programming")
element.send_keys(Keys.ENTER)

# Wait to see the search results
time.sleep(10)

# Close the browser
driver.quit()

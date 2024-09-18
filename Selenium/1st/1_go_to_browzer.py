import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# Set up the WebDriver (make sure to provide the correct path to your WebDriver)
driver_path = 'E:/Dowmnload/Driver/chromedriver.exe'  # Update this path
service = Service(driver_path)
driver = webdriver.Chrome(service=service) # Initialize the WebDriver

# Load the website
url = 'https://www.flipkart.com/'
driver.get(url)
time.sleep(10)  # Adjust the wait time as needed

# # Wait for the element to be clickable. Click a button or link and go to another page.
driver.find_element(By.XPATH, """/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div/div/div[2]/div[1]/div/div[1]/div/div/div/div/div[1]/a[4]""").click()

time.sleep(500)  # Wait for 5 seconds
driver.quit()


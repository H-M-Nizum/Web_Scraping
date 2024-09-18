import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver_path = "E:/Dowmnload/Driver/chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
url = "https://www.nike.com/w/mens-shoes-nik1zy7ok"
driver.get(url)
time.sleep(10)
driver.find_element(By.XPATH, """/html/body/div[6]/div/div/div/div/section/div[1]/button""").click()
time.sleep(10)
while True:
    height = driver.execute_script("return document.body.scrollHeight")
    print(height)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(5)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if height == new_height:
        break
time.sleep(10)
driver.quit()
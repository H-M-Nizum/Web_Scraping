import pandas as pd
from bs4 import BeautifulSoup
import requests

url = "https://github.com/topics"
r = requests.get(url)
print(r)

soup = BeautifulSoup(r.text, "lxml")
a = soup.find_all('form', class_="ajax-pagination-form js-ajax-pagination")

print(a)
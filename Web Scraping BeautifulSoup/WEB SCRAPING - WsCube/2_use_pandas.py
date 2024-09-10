import requests
from bs4 import BeautifulSoup
import pandas

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
# print(soup.span)
# print(soup.a)
# _________________________ Extract all laptop name -------------------------------
name = soup.find_all('a', class_="title")
# print(name)
product_name = []
for i in name:
    product_name.append(i.text)
# print(product_name)

# _________________________ Extract all laptop price -------------------------------

price = soup.find_all('h4', class_="price")
# print(price)
product_price = []
for i in price:
    product_price.append(i.text)
# print(product_price)
# _________________________ Extract all laptop description  -------------------------------

description  = soup.find_all('p', class_="description")
# print(price)
product_description = []
for i in description :
    product_description .append(i.text)
# print(product_description )
# _________________________ Extract all laptop rating  -------------------------------

rating  = soup.find_all('p', class_="data-rating")
# print(price)
product_rating = []
for i in rating :
    product_rating .append(i.text)
print(product_rating )


df = pandas.DataFrame({"product name": product_name, "price": product_price, "description" : product_description})

print(df)
df.to_csv("laptop_data.csv")
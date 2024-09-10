import requests
from bs4 import BeautifulSoup
import pandas

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")

# 
name = soup.find_all('a', class_="title")
product_name = []
for i in name:
    product_name.append(i.text)

#
price = soup.find_all('h4', class_="price")
product_price = []
for i in price:
    tem = i.text
    product_price.append(tem)

#
description  = soup.find_all('p', class_="description")
product_description = []
for i in description :
    product_description .append(i.text)

#
rating  = soup.find_all('div', class_="ratings")
product_rating = []
for i in rating :
    product_rating.append(len(i.find_all('span')))

#
review  = soup.find_all('p', class_="review-count float-end")
product_Review = []
for i in review :
    product_Review.append(i.text)

#
dic = {
    "Product Name" : product_name,
    "Product Price" : product_price,
    "Product Description" : product_description,
    "Product Rating" : product_rating,
    "Product Review" : product_Review
}
df = pandas.DataFrame(dic)
print(df)
df.to_csv("laptop_data1.csv")
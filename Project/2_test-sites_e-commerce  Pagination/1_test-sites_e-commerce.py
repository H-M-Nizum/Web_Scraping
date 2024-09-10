import requests
from bs4 import BeautifulSoup
import pandas


product_name = []
product_price = []
product_description = []
product_rating = []
product_Review = []
for i in range(1, 21):
    url = f"https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={i}"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    # 
    name = soup.find_all('a', class_="title")
    for i in name:
        product_name.append(i.text)

    #
    price = soup.find_all('h4', class_="price")
    for i in price:
        tem = i.text
        product_price.append(tem)

    #
    description  = soup.find_all('p', class_="description")
    for i in description :
        product_description .append(i.text)

    #
    rating  = soup.find_all('div', class_="ratings")
    for i in rating :
        product_rating.append(len(i.find_all('span')))

    #
    review  = soup.find_all('p', class_="review-count float-end")
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
df.to_csv("laptop_data_pagination.csv")
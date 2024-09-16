import pandas as pd
from bs4 import BeautifulSoup
import requests
names = []
prices = []
descriptions = []
reviews = []
ratings = []
# Send HTTP request
for i in range(1,21):
    url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=" + str(i)
    r = requests.get(url)
    # print(r)

    soup = BeautifulSoup(r.text, "lxml")
    data_container = soup.find_all('div', class_="product-wrapper card-body")
    for data in data_container:
        name = data.find('a', class_='title')
        names.append(name.text)
        price = data.find('h4', class_="price float-end card-title pull-right")
        prices.append(price.text)
        description = data.find('p', class_="description card-text")
        descriptions.append(description.text)
        review = data.find('p', class_="review-count float-end")
        reviews.append(review.text)
        rating = data.find_all('span', class_="ws-icon ws-icon-star")
        ratings.append(len(rating) * '⭐')
    # lin = soup.find('a', class_="page-link")    
    # url = "https://webscraper.io" + lin.get('href')
    # print(url)
df = pd.DataFrame({"Name":names, "Price":prices, "Description":descriptions, "Review":reviews, "Rating":ratings})
df.to_csv("E:\\Github_New\\Web_Scraping\\Project\\4_test_sites_E-commerce_with_pagination\\laptop_pagination.csv")

import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

url = "https://ticker.finology.in/"

r = requests.get(url)
soup = bs(r.text, 'html.parser')

table = soup.find('table')

header_data = []
header = table.find_all('th')
for i in header:
    header_data.append(i.text)
# print(header_data)

df2 = pd.DataFrame(columns=header_data)

row = table.find_all('tr')
for i in row[1:]:
    data = i.find_all("td")
    ro = [tr.text.strip("\n") for tr in data]
    l = len(df2)
    df2.loc[l] = ro
print(df2)

df2.to_csv("ticker_data.csv")
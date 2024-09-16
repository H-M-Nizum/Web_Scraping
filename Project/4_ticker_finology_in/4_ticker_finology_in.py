from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://ticker.finology.in/"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

div1 = soup.find('div', class_="tab-content", id="pills-tabContent")
table_data = div1.find_all('table', class_="table table-sm table-hover screenertable")
t_data = []
for table in table_data:
    header = []
    t1 = table.find_all('th')
    for i in t1:
        header.append(i.text)
 
    # find row
    row = table.find_all('tr')
    # print(row)
    for j in row:
        td1 = j.find_all('td')
        if td1:
            t_data.append([x.text.replace("\n", "") for x in td1])

df = pd.DataFrame(t_data, columns=header)
df.to_csv("E:\\Github_New\\Web_Scraping\\Project\\4_ticker_finology_in\\ticker_table.csv")
print(df)

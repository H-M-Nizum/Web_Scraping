from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://ticker.finology.in/market/"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

# Get table page url endpoint ---------------------------------
a_tags = soup.find_all('a', class_="card cardscreen cardtoolbar")
tag_url = []
for i in a_tags:
    tag_url.append(i.get('href'))
print(tag_url)

base_url = 'https://ticker.finology.in'
for i in tag_url:
    b_url = base_url + i
    csv_file_name = i.split('/')[2]
    csv_data = []
    web = requests.get(url)
    soup_web = BeautifulSoup(web.text, 'lxml')
    for x in soup_web.find_all('tbody'):
        row =  x.find_all('tr')
        for j in row:
            csv_data.append([x.text for x in j.find_all('td')])
        
    
    csv_file_name = i.split('/')[2]
    df = pd.DataFrame(csv_data)
    df.to_csv(f"{csv_file_name}.csv")
    print(csv_file_name)
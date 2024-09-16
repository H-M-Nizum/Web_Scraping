import pandas as pd
from bs4 import BeautifulSoup
import requests

url = 'https://webscraper.io/test-sites/tables'

r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
table_data = []

tables = soup.find_all('table', class_="table table-bordered")
# Loop through each table found
for table in tables:
    # Get table headers
    headers = [header.text for header in table.find_all('th')]
    # Get all the rows of the table
    rows = table.find_all('tr')
    # Extract data from each row
    for row in rows:
        columns = row.find_all('td')
        if columns:
            table_data.append([column.text for column in columns])

table2 = soup.find_all('table', class_="table table-bordered table-bordered2")
for table in table2:
    # Get all the rows of the table
    rows = table.find_all('tr')
    # Extract data from each row
    for row in rows:
        columns = row.find_all('td')
        if columns:
            table_data.append([column.text for column in columns])

# Create a DataFrame using the headers and table data
df = pd.DataFrame(table_data, columns=headers)
print(df)

# Create csv file
df.to_csv('E:\\Github_New\\Web_Scraping\\Project\\3_test_sites_e-commerce_table_data\\table_data.csv')



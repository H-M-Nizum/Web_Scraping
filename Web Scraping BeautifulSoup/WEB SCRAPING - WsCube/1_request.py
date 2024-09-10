import requests

url = "https://www.cricbuzz.com"
r = requests.get(url)
print(r.status_code)
print(r.text)
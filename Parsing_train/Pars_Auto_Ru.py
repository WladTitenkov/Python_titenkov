import random
from time import sleep
import requests
from bs4 import BeautifulSoup
import json
import csv

url = "https://auto.ru/cars/toyota/sienna/all/?geo_id="
url2="https://auto.ru/cars/used/sale/toyota/sienna/1105696878-49374540/"
#
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.0.1996 Yowser/2.5 Safari/537.36"
    }

req = requests.get(url, headers=headers, allow_redirects=True)
req.encoding = 'Unicode'
src = req.text

def save_from_www(link, filename):
    print(filename)
    r = requests.get(link, headers=headers, allow_redirects=True)
    open(filename, "wb").write(r.content)
save_from_www(url, 'auto.html')
save_from_www(url2, "page.html")
# with open("auto.html", "r") as f:
#     src = f.read()

soup = BeautifulSoup(src, "lxml")


page_all_name = soup.find_all("a", class_="Link ListingItemTitle__link")
i = 0
for n in page_all_name:
    i += 1
    # print(type(n))
    print(n.text)
    print(n.get('href'))

print(f'Всего авто: {i}')

import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com/Brawny-Regular-Square-Options-Quarter/dp/B08RT1NF23/ref=sr_1_1_sspa?dchild=1&keywords=paper+towel+bounty&qid=1619016986&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExNEcwQ09LMDUwWFQ5JmVuY3J5cHRlZElkPUEwOTY1MDk2Mlg3NURGVDdCMzhaSCZlbmNyeXB0ZWRBZElkPUEwNjI2OTAyMUZNWjIyRk00UTBHRCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 '
                  'Safari/537.36'}
page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle")

print(title)

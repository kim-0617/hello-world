### 셀렉터를 이용한 삼성전자 일별시세 조회
import requests
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0'}
url = 'https://finance.naver.com/item/sise_day.naver?code=005930&page=1'
res = requests.get(url, headers=headers)

# print("73,300" in res.text)
soup = BeautifulSoup(res.text, 'html5lib')
css_selctor = "body > table.type2 > tbody > tr > td:nth-child(2) > span"
result = soup.select(css_selctor)

for item in result:
    print(item.text)
### 삼성전자 일별시세 데이터 조회
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

url = 'https://finance.naver.com/item/sise_day.naver?code=005930&page=1'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

table = soup.find('table', attrs={"class":"type2"}).find_all("tr")

temp_list = []
table_list = []
cols_list = []

for t in table:
    data = t.find_all('span') # 데이터
    cols = t.find_all('th') # 컬럼명
    
    for c in cols:
        cols_list.append(c.get_text().strip()) # 컬럼

    for d in data:
        temp_list.append(d.get_text().strip()) # 임시리스트에 저장

    if temp_list:
        table_list.append(temp_list[:]) # 한줄씩 데이터 저장
    temp_list.clear()

df = pd.DataFrame(table_list, columns=cols_list)
print(df)
# df.to_excel('S_data.xlsx')
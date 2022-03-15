import requests
import csv
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=" 

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="") # newline을 저래하지 않으면 불필요한 개행이 생긴다
writer = csv.writer(f)

col_names = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
writer.writerow(col_names)

for page in range(1,5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    date_rows = soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("tr")
    for row in date_rows:
        columns = row.find_all("td")
        if len(columns) <= 1:  # 데이터가 있는 tr은 td속성을 여러개 갖고 있는데 단지 줄바꿈을 위한 tr은 td를 한개만 갖고있다.
            continue
        data = [column.get_text().strip() for column in columns]
        # print(data)
        writer.writerow(data)
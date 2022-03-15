### 주가데이터 정보조회 - POST 메서드로 가져온 정보를 JSON모듈로 리스트화 -> 데이터 프레임으로
import requests
import json
import pprint
import pandas as pd
import matplotlib as plt

url = 'https://api.finance.naver.com/siseJson.naver?\
symbol=005930\
&requestType=1\
&startTime=20211224\
&endTime=20220129\
&timeframe=day'

# symbol = 주가종목
# startTime = 시작일
# endTime = 종료일
# timeframe = 일 / 월 / 연 선택
res = requests.post(url)

data = res.text.replace("'",'"').strip()
data = json.loads(data)
# pprint.pprint(data)

df = pd.DataFrame(data[1:],columns=data[0])
df.set_index('날짜',inplace=True)
print(df)

df.to_excel('data.xlsx')



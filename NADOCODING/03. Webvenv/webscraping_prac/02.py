### 공지사항 첨부파일 스크래핑
import requests
from bs4 import BeautifulSoup
import json
import time # 너무 과부하 요청하지 않게 쉬었다가

for page in range(2,3):
    url = f'https://www.fss.or.kr/fss/bbs/B0000190/list.do?menuNo=200221&bbsId=&cl1Cd=&pageIndex={page}&sdate=&edate=&searchCnd=1&searchWrd='
    res = requests.get(url)

    soup = BeautifulSoup(res.text, "html5lib")
    sel = '#content > div.bd-list > table > tbody > tr > td.title > a'
    titles = soup.select(sel)

    for tag in titles:
        sub_url = "https://www.fss.or.kr" + tag['href']
        res = requests.get(sub_url) # 게시글로 이동
        soup = BeautifulSoup(res.text, 'html5lib')

        sel = '#content > div.bd-view > dl.file-list > dd > div > div > a'
        links = soup.select(sel) 

        for link in links:
            download_url = 'https://www.fss.or.kr' + link['href'] 
            res = requests.get(download_url) # 여기서 얻어온 값을 file로 저장만 해준다면 (다운로드 링크로 이동)

            file_name = link.text.strip().replace('\t','')
            file_name = file_name.split('\n')[0] # 파일이름 가공
            
            with open(r'C:\Users\PC\Desktop\here\\' + file_name, "wb") as f:
                f.write(res.content)

        time.sleep(1)

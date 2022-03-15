### 멜론 탑 100 크롤링 -> 좋아요 수 크롤링 실패
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from selenium import webdriver
import time
import urllib.request
import pandas as pd

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'}

url = 'https://www.melon.com/chart/index.htm'
res = requests.get(url,headers = header)
soup = BeautifulSoup(res.text,"html.parser")

melon_lst = []
cols = ['Rank','Song','Singer','Album']

sel = '.lst50,.lst100'
content = soup.select(sel)

for c in content:
    rank = c.find('span', attrs={'class':'rank'}).get_text()
    song_name = c.find('div', attrs={'class':'ellipsis rank01'}).a.text.replace('\n','')
    singer = c.find('div', attrs={'class':'ellipsis rank02'}).a.text.replace('\n','')
    album = c.find('div', attrs={'class':'ellipsis rank03'}).a.text.replace('\n','')
    
#     print(f"순위 : {rank}")
#     print(f"제목 : {song_name}")
#     print(f"가수 : {singer}")
#     print(f"앨범 : {album}")
#     print()
    
    melon_lst.append([rank,song_name,singer,album])
    
df = pd.DataFrame(melon_lst, columns=cols).set_index('Rank')
df.to_csv("Melon100.csv",encoding='utf-8-sig')
### 구글 검색결과 이미지 스크래핑
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from selenium import webdriver
import time
import urllib.request

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'}

word = input('검색어를 입력하세요>>>')
keyword = quote_plus(word)
url = f'https://www.google.com/search?q={keyword}\
&sxsrf=APq-WBuavLGnZiRJZCZqCSaSV3yVlZndmA:1643818149478\
&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj4u__ms-H1AhUKRd4KHeDuCdgQ_AUoAXoECAIQAw\
&biw=1536&bih=714&dpr=1.25'

browser = webdriver.Chrome(options=chrome_options)
browser.get(url)
time.sleep(2)
html = browser.page_source

SCROLL_PAUSE_SEC = 1

# 스크롤 높이 가져옴
last_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # 끝까지 스크롤 다운
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 1초 대기
    time.sleep(SCROLL_PAUSE_SEC)

    # 스크롤 다운 후 스크롤 높이 다시 가져옴
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    
soup = BeautifulSoup(html,"html.parser")

title = soup.find_all('img', attrs={'class':'rg_i Q4LuWd'})

for t in title:
    img_url = t.get('src')
    file_name = t.get('alt')
    
    rule_lst = ['/' ,'\\', '?', '%', '*', ':', '|', '"', '<', '>', '.']       
    for rule in rule_lst:
        if rule in file_name:
            file_name = file_name.replace(rule,'')

    if img_url:
        urllib.request.urlretrieve(str(img_url), "../img/" + file_name + ".png")
    else:
        img_url = t.get('data-src')
        urllib.request.urlretrieve(str(img_url), "../img/" + file_name + ".png")
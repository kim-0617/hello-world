### 네이버 검색결과 이미지 스크래핑
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
url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=' + keyword

browser = webdriver.Chrome(options=chrome_options)
browser.get(url)
time.sleep(2)
html = browser.page_source

soup = BeautifulSoup(html,"html.parser")

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

sel = '#main_pack > section.sc_new.sp_nimage._prs_img._imageSearchPC > div > div.photo_group._listGrid > div.photo_tile._grid > div > div > div.thumb > a > img'
title = soup.select(sel)

for t in title:
    img_url = t.get('src')
    
    file_name = t.get('alt')
    
    rule_lst = ['/' ,'\\', '?', '%', '*', ':', '|', '"', '<', '>', '.']       
    for rule in rule_lst:
        if rule in file_name:
            file_name = file_name.replace(rule,'')
    
    urllib.request.urlretrieve(str(img_url), "./img/" + file_name + ".png")
    
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

word = input("검색어를 입력하세요 >>> ")
keyword = quote_plus(word)

for page in range(1,3): # 1~2 page 검색
    url = f'https://section.blog.naver.com/Search/Post.naver?pageNo={page}&rangeType=ALL&orderBy=sim&keyword=' + keyword
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(url)

    html = browser.page_source
    soup = BeautifulSoup(html,"html.parser")

    blocks = soup.find_all('div', attrs = {'class':'info_post'})
    print(f"------------------------------------------------------------------{page}페이지\n------------------------------------------------------------------")
    for block in blocks:
        title = block.find('strong', attrs = {'class':'title_post'}).get_text() 
        link =  block.find('a', attrs = {'class':'desc_inner'})['href']

        print(f"글 제목: {title}")
        print(f"링크: {link}")
        print()
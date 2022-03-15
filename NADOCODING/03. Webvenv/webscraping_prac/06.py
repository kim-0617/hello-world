### 인스타 이미지 크롤링
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from selenium import webdriver
import time
import urllib.request
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import os
import datetime

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'}

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

browser = webdriver.Chrome(options=chrome_options)
    
login_url = 'https://www.instagram.com/accounts/login/'
browser.get(login_url)
browser.maximize_window()
browser.implicitly_wait(3)
id = "seonghyeon2011"
pw = "ksh5993!!"

try:
    browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(id)
    browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(pw)
    browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
    time.sleep(3)
except:
    pass

# ### 내가조작 하는 부분 로그인 잘 되면 안해도 됨###
# # input('press any key to run : ') 

word = input("검색어를 입력하세요 >>> ")
keyword = quote_plus(word)

if not os.path.exists("./Webvenv/webscraping_prac/img/" + word): 
    os.mkdir("./Webvenv/webscraping_prac/img/" + word)

url = f'https://www.instagram.com/explore/tags/{keyword}/'
browser.get(url)

WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/section/main/header/div[2]/div/div[1]/h1')))

###################################################################################################################################
SCROLL_PAUSE_SEC = 3

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
###################################################################################################################################

html = browser.page_source
soup = BeautifulSoup(html,'html.parser')

images = soup.select('.FFVAD')

for idx,i in enumerate(images):
    try:
        if i['src']:
            img_url = i['src']
        else:
            img_url = i['srcset src']

        now = datetime.datetime.now()
        now = time.strftime("%Y%M%d_%H%M%S")

        file_name = word + str(now) + ".png"
        time.sleep(1)

        urllib.request.urlretrieve(str(img_url), "./Webvenv/webscraping_prac/img/" + word + "/" + file_name)
    except:
        pass
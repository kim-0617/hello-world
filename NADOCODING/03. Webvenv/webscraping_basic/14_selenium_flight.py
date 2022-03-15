from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/"
browser.get(url)

browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").send_keys('\n') # 가는날
time.sleep(0.5)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[4]').click() # 가는날짜
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[6]/td[2]').click() # 오는날짜

browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]/i').click() # 장소 선택
time.sleep(0.5)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/section/section/button[1]').click() # 국내 선택
time.sleep(0.5)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/section/section/div/button[2]/i[1]').click() # 제주도 선택
time.sleep(0.5)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/button').click() # 검색

# 로딩을 기다리기 위해 처리
try:
    elem = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/div/div[1]/div[5]/div/div[2]/div[2]')))
    print(elem.text)

finally:
    browser.quit()



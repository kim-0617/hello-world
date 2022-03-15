import imp
from lib2to3.pgen2 import driver
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

browser = webdriver.Chrome("./Webvenv/webscraping_basic/chromedriver.exe")
# browser.maximize_window() # 창 최대화

url = "https://www.naver.com/"
time.sleep(random.uniform(1,3))
browser.get(url)

browser.find_element_by_class_name("link_login").click()
input_js = ' \
        document.getElementById("id").value = "{id}"; \
        document.getElementById("pw").value = "{pw}"; \
    '.format(id = "test_id", pw = "test_pw")
time.sleep(random.uniform(1,3)) # 자동화탐지를 우회 하기 위한 delay
browser.execute_script(input_js)
time.sleep(random.uniform(1,3)) # 자동화탐지를 우회 하기 위한 delay
browser.find_element_by_id("log.login").click()



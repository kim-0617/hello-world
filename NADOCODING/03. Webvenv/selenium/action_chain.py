from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Chrome()
url = 'https://google.com'
browser.get(url)

action = ActionChains(browser)
browser.find_element_by_css_selector('.gb_1').click()
action.send_keys('kimsh5993@gmail.com').perform()
action.send_keys('\n').perform()

### 차례대로 명령어를 입력하고 마지막에 perform()
# action.send_keys('\n').send_keys('\n').send_keys('\n').send_keys('\n').perform()
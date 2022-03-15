from lib2to3.pgen2.token import RPAR
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/html/')
browser.maximize_window()

time.sleep(3)

# 특정 영역 스크롤
elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[61]')

# 방법1 : ActionChain / elem이 보이도록 스크롤을 내림
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()

# 방법2 : elem이 있는 좌표정보를 가져옴
# xy = elem.location_once_scrolled_into_view # 함수 아님
# print("type : ", type(xy))
# print("value : ", xy)
# elem.click()



time.sleep(3)
browser.quit()
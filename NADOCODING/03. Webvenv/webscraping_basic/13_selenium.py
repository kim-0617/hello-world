from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("http://naver.com")

elem = browser.find_element_by_class_name("link_login")
elem.click()

browser.find_element_by_id("id").send_keys("kkk5993")
browser.find_element_by_id("pw").send_keys("ksh5993!!")

browser.find_element_by_class_name("btn_login").click()

time.sleep(2)

# # id를 새로 입력 / 잘못된 id일 때 지우고 다시입력
# browser.find_element_by_id("id").clear()
# browser.find_element_by_id("id").send_keys("my_id")

# html 정보 출력
print(browser.page_source)

# browser 종료
browser.quit()
# browser.close() -> 현재 탭만 종료
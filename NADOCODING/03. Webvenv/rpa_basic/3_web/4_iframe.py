from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio")

browser.switch_to.frame('iframeResult') # iframe이 있는 경우 프레임 전환을 해줘야 한다. iframe의 id 값을 입력해야 한다

elem = browser.find_element_by_xpath('//*[@id="html"]')
elem.click()

browser.switch_to.default_content() # 그 프레임 내에서 작업을 마쳤다면, 원상복구해서 다른 작업을 계속할 수 있다.

time.sleep(3)
browser.quit()
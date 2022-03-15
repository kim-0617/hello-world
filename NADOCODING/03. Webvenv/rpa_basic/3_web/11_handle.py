from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.w3schools.com/tags/att_input_type_radio.asp')
curr_handle = browser.current_window_handle
print("처음 핸들 : ", curr_handle)

elem = browser.find_element(By.XPATH,'//*[@id="main"]/div[2]/a').click()

handles = browser.window_handles # 모든 핸들 정보
for handle in handles:
    print("각 창의 핸들 : ", handle)
    browser.switch_to.window(handle) # 각 핸들로 이동해서
    print('타이틀 : ',browser.title)
    print()

# 열려있는 창 종료
browser.close()

# 이전 핸들로 돌아오기
browser.switch_to.window(curr_handle)
print('돌아온 타이틀!!!!!!! : ', browser.title)

time.sleep(3)
browser.quit()
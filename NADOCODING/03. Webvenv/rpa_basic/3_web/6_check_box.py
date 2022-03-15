from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox")

browser.switch_to.frame('iframeResult')

# //*[@id="vehicle1"]
# //*[@id="vehicle2"]
# //*[@id="vehicle3"]
elem1 = browser.find_element_by_xpath('//*[@id="vehicle1"]')
elem1 = browser.find_element(By.XPATH,'//*[@id="vehicle1"]') # 위문장과 동일한 의미
# elem2 = browser.find_element_by_xpath('//*[@id="vehicle2"]')
# elem3 = browser.find_element_by_xpath('//*[@id="vehicle3"]')

if elem1.is_selected() == False:
    elem1.click()
else:
    pass
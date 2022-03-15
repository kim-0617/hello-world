from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option')

browser.switch_to.frame('iframeResult')

# elem = browser.find_element_by_xpath('//*[@id="cars"]/option[3]')
# elem.click()

# # 텍스트 값을 통해서 선택 []에 인덱스 지우고 text()="텍스트값"
# elem = browser.find_element_by_xpath('//*[@id="cars"]/option[text()="Audi"]')
# elem.click()

# 부분 일치하는 텍스트값을 통해 항목선택 contains(text(),"Au")
elem = browser.find_element_by_xpath('//*[@id="cars"]/option[contains(text(),"Au")]')
elem.click()
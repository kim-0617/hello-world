from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/')
browser.maximize_window()

browser.find_element_by_xpath('//*[@id="main"]/div[2]/div/div[1]/a[1]').click() # learn html
browser.find_element_by_xpath('//*[@id="topnav"]/div/div/a[10]').click() # How To
browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]').click() # Contact Form

FirstName = "나도"
LastName = "코딩"
Country = "Canada"
Subject = "퀴즈 완료하였습니다."

browser.find_element_by_xpath('//*[@id="fname"]').send_keys(FirstName)
browser.find_element_by_xpath('//*[@id="lname"]').send_keys(LastName)
browser.find_element_by_xpath(f'//*[@id="country"]/option[text()="{Country}"]').click()
browser.find_element_by_xpath('//*[@id="main"]/div[3]/textarea').send_keys(Subject)

browser.execute_script('window.scrollTo(0,500)')

time.sleep(3)
browser.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()

time.sleep(3)
browser.quit()
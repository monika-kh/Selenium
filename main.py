from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

browser = webdriver.Firefox(executable_path='./geckodriver')
browser.get('http://gmail.com')
action = webdriver.ActionChains(browser)
# emailElem = browser.find_element_by_id('identifierId')
# emailElem.send_keys("mailtest081991@gmail.com")
# browser.find_element_by_id('identifierNext').click()
# # browser.get('https://accounts.google.com/ServiceLogin?         service=mail&continue=https://mail.google.com/mail/#password')
# print("passwordElem================", browser)
# passwordElem = browser.find_element_by_name('password')
# passwordElem.send_keys("test@1234")
# browser.find_element_by_id('passwordNext').click()


email_phone = browser.find_element_by_xpath("//input[@id='identifierId']")
email_phone.send_keys("mailtest081991@gmail.com")
browser.find_element_by_id("identifierNext").click()
password = WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))
)
password.send_keys("test@1234")


browser.find_element_by_xpath('//button[text()="Next"]').click()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def Simple_Window():
    browser = webdriver.Firefox()
    time.sleep(2)
    browser.get('http://www.swagbucks.com/p/login')
    time.sleep(5)
    browser.find_element_by_id('sbxJxRegEmail').send_keys('benjaminehuddle@gmail.com')
    time.sleep(5)
    browser.find_element_by_class_name('recaptcha-anchor').click()
    time.sleep(5)
    raw_input('Press enter to continue after CAPCHA & logging in')
    time.sleep(5)
    browser.find_element_by_id('loginBtn').click()
    time.sleep(30)
    browser.find_element_by_id('sbGlobalNavSearchInputWeb').send_keys('Cats and dogs')
    time.sleep(1)
    browser.find_element_by_id('sbGlobalNavSearchInputWeb').send_keys(Keys.ENTER)
    time.sleep(60)
    browser.quit()

Simple_Window()
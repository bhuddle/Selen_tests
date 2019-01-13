from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def Simple_Window():
    browser = webdriver.Chrome('C:\Python27\ChromeDriver\chromedriver.exe')
    time.sleep(2)
    browser.get('http://www.swagbucks.com/p/login')
    time.sleep(5)
    raw_input('Press enter to continue after CAPCHA & logging in')
    time.sleep(20)
    """ Need to get past capcha
    browser.find_element_by_id('sbLogInCta').click()
    time.sleep(5)
    browser.find_element_by_id('sbxJxRegEmail').send_keys('test@email.com')
    time.sleep(5)
    browser.find_element_by_id('sbxJxRegPswd').send_keys('1234')
    time.sleep(5)
    browser.find_element_by_class_name('recaptcha-anchor').click()
    time.sleep(5)
    browser.find_element_by_id('loginBtn').click()"""
    browser.find_element_by_id('sbGlobalNavSearchInputWeb').send_keys('Cats and dogs')
    time.sleep(1)
    browser.find_element_by_id('sbGlobalNavSearchInputWeb').send_keys(Keys.ENTER)
    time.sleep(60)
    browser.quit()

Simple_Window()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def Simple_Window():
    browser = webdriver.Chrome('location of chrome.exe')
    time.sleep(2)
    browser.get('https://www.swagbucks.com/p/login')
    time.sleep(5)
    browser.find_element_by_id('sbxJxRegEmail').send_keys('benjaminehuddle@gmail.com')
    time.sleep(5)
    raw_input('Press enter to continue after CAPCHA & logging in')
    time.sleep(30)
    browser.get('https://www.swagbucks.com/surveys')
    time.sleep(30)
    browser.find_element_by_class_name('surveyLink startSurveyLink').click()
    time.sleep(120)
    
    browser.quit()

Simple_Window()
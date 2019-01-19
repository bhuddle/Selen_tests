from selenium import webdriver
import time

def Check_Search():
    url = 'http://www.powinenergy.com/news'
    browser = webdriver.Chrome('C:\Python27\ChromeDriver\chromedriver.exe')
    browser.maximize_window()
    browser.implicitly_wait(10)
    time.sleep(5)
    browser.get(url)
    time.sleep(5)
    
    """
    Go to website
    Enter in Ascii characters
    Enter in non ascii characters
    Enter in max # of characters - 256?
    Escape sequence
    enter in None
    """
    
    time.sleep(5)
    browser.quit()

Check_Search()
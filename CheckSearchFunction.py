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
    
    testText = []
    testText.append('Normal Search')
    testText.append('1/19/2019')
    testText.append('&#160;')
    testText.append('&#160')
    testText.append(u'\xe8 \xe9 \xe10 \xc3 \xc4 \xc5')
    testText.append('`~`234!@#$%^&)(*+_-=+')
    testText+='^\ \\ \\\\ ^^'.split()
    testText.append('')
    longword = ''
    for a in range(0,257):
        longword = longword + 'W'
    testText.append(longword)
    
    for test in testText:
        searchBar = browser.find_element_by_id('s')
        searchButton = browser.find_element_by_id('searchsubmit')
        searchBar.clear()
        searchBar.send_keys(test)
        searchButton.click()
        time.sleep(5)
        browser.get(url)
        time.sleep(5)
       
    time.sleep(5)
    browser.quit()

Check_Search()
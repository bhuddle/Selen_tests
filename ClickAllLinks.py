from selenium import webdriver
import time

def Check_Links():
    url = 'http://www.powinenergy.com/news'
    browser = webdriver.Chrome('C:\Python27\ChromeDriver\chromedriver.exe')
    browser.maximize_window()
    browser.implicitly_wait(10)
    time.sleep(5)
    browser.get(url)
    time.sleep(5)
    links = browser.find_elements_by_xpath('//a[@href]')
    print "Number of links: "+str(len(links)) 
    for link in range(len(links)):
        link2 = str(links[link].get_attribute('href'))
        if '#' in link2 or '@' in link2 or 'tel' in link2:
            print "Skipping:  "+str(links[link].get_attribute('href'))       
        else:
            print "Clicking: "+str(links[link].get_attribute('href'))
            links[link].click()
            time.sleep(5)
            browser.get(url)
            time.sleep(5)
            links = browser.find_elements_by_xpath('//a[@href]')
    print "all links clicked"
    time.sleep(5)
    browser.quit()

Check_Links()


"""
for checking with assertion:
url = browser.get_current_url()
assert url in "url.com/to/test"
"""
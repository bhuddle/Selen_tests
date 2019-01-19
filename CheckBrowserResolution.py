from selenium import webdriver
import time

def get_Res(res):
    res = res.split('x')
    return res[0],res[1]

def Check_Res():
    url = 'http://www.powinenergy.com/news'
    res = '1366x768,1920x1080,1280x800,320x568,1440x900,1280x1024,320x480,1600x900,768x900,360x640'
    res = res.split(',')
    
    browser = webdriver.Chrome('C:\Python27\ChromeDriver\chromedriver.exe')
    browser.set_window_position(10,10)
    
    for n in res:
        x,y = get_Res(n)
        print 'Window Size: '+x+'x'+y
        time.sleep(5)
        browser.get(url)
        browser.set_window_size(x,y)
        time.sleep(5)
    print 'Window Size: Maximized'
    browser.maximize_window()
    time.sleep(5)
    browser.quit()

Check_Res()
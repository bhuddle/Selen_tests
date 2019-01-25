from selenium import webdriver
import time

def get_Res(res):
    res = res.split('x')
    return res[0],res[1]

def test_Check_Res():
    url = 'http://www.powinenergy.com/news'
    res = '1036x720'
    #Not working with Jenkins '1366x768,1920x1080,1280x800,320x568,1440x900,1280x1024,320x480,1600x900,768x900,360x640'
    res = res.split(',')
    
    browser = webdriver.Chrome('C:\Python27\ChromeDriver\chromedriver.exe')
    browser.set_window_position(10,10)
    browser.get(url)
    
    for n in res:
        x,y = get_Res(n)
        print 'Window Size: '+x+'x'+y
        time.sleep(5)
        browser.set_window_size(x,y)
        time.sleep(5)
        assert browser.get_window_size()['width'] == int(x) and browser.get_window_size()['height'] == int(y)
    print 'Window Size: Maximized'
    time.sleep(5)
    browser.quit()
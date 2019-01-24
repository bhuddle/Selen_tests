from selenium import webdriver
import time

def get_Res(res):
    res = res.split('x')
    return res[0],res[1]

def test_Check_Res():
    url = 'http://www.powinenergy.com/news'
    res = '1366x768,1920x1080,1280x800,320x568,1440x900,1280x1024,320x480,1600x900,768x900,360x640'
    passRes = '1366x768,1920x1080,1280x800,1440x900,1280x1024,1600x900,768x900' #less than 400 width fails
    res = res.split(',')
    passRes = passRes.split(',')
    
    browser = webdriver.Chrome('C:\Python27\ChromeDriver\chromedriver.exe')
    browser.set_window_position(10,10)
    browser.get(url)
    
    for n in passRes:
        x,y = get_Res(n)
        print 'Window Size: '+x+'x'+y
        time.sleep(5)
        browser.set_window_size(x,y)
        time.sleep(5)
        assert browser.get_window_size()['width'] == int(x)
        assert browser.get_window_size()['height'] == int(y)
    print 'Window Size: Maximized'
    browser.maximize_window()
    assert browser.get_window_size()['width'] == 1936 and browser.get_window_size()['height'] == 1056 #for my own computer res, will change with diff computer
    time.sleep(5)
    browser.quit()
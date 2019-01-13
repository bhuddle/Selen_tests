from selenium import webdriver
import pyautogui
from selenium.webdriver.common.keys import Keys
import time

def Simple_Window():
    #depends on screen size and location
    btn1 = {'x':954 , 'y':566}
    btn2 = {'x':974 , 'y':560}
    btn3 = {'x':956 , 'y':609}
    btn4 = {'x':958 , 'y':654}
    btn5 = {'x':959 , 'y':698}  
    
    browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
    time.sleep(2)
    browser.get('https://www.swagbucks.com/p/login')
    time.sleep(5)
    browser.find_element_by_id('sbxJxRegEmail').send_keys('benjaminehuddle@gmail.com')
    time.sleep(5)
    raw_input('Press enter to continue after CAPCHA & logging in')
    time.sleep(30)
    browser.get('https://www.swagbucks.com/surveys')
    time.sleep(30)
    #hopefully this starts a survey
    pyautogui.click(btn1['x'], btn1['y'])
    raw_input('exit if survey started with CTRL+C')
    
    browser.quit()

Simple_Window()
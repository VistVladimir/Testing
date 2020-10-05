from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)
browser.find_element_by_css_selector("body > form > div > div > button").click()
alert = browser.switch_to.alert
alert.accept()
gg = browser.find_element_by_id("input_value")
x = gg.text
y = calc(x)
fot = browser.find_element_by_id("answer")
fot.send_keys(y)
gg3 = browser.find_element_by_css_selector("body > form > div > div > button")
gg3.click()
time.sleep(10)
browser.quit()


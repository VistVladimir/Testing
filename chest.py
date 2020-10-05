from selenium import webdriver
import time
import math

def calc(gg1):
    return str(math.log(abs(12*math.sin(int(gg1)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(2)
gg = browser.find_element_by_id("treasure")
gg1 = gg.get_attribute("valuex")
gg12 = calc(gg1)
gg3 = browser.find_element_by_id("answer")
gg3.send_keys(gg12)
gg4 = browser.find_element_by_id("robotsRule")
gg4.click()
gg41 = browser.find_element_by_id("robotCheckbox")
gg41.click()
gg5 = browser.find_element_by_css_selector("body > div > form > div > div > button")
gg5.click()
time.sleep(10)
browser.quit()

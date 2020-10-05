from selenium import webdriver
import time
import math

def calc(gg):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
gg = browser.find_element_by_id("input_value")
x = gg.text
y = calc(gg)
fot = browser.find_element_by_id("answer")
fot.send_keys(y)
gg1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
gg1.click()
gg2 = browser.find_element_by_css_selector("[for='robotsRule']")
browser.execute_script("return arguments[0].scrollIntoView(true);", gg2)
gg2.click()
gg3 = browser.find_element_by_css_selector("body > div > form > button")
gg3.click()
time.sleep(10)
browser.quit()

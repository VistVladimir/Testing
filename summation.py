from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
num1 = int(browser.find_element_by_id("num1").text)
num2 = int(browser.find_element_by_id("num2").text)
y = num1 + num2
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(y))
browser.find_element_by_css_selector("body > div > form > button").click()
time.sleep(10)
browser.quit()
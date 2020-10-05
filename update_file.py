from selenium import webdriver

import time
import os


try: 
    
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)    
    # Ваш код, который заполняет обязательные поля
    
    form1 = browser.find_element_by_xpath("/html/body/div/form/div/input[1]")
	
    form1.send_keys("Leon")
	
    form2 = browser.find_element_by_xpath("/html/body/div/form/div/input[2]")
	
    form2.send_keys("Kennedy")
	
    form3 = browser.find_element_by_xpath("/html/body/div/form/div/input[3]")
    form3.send_keys("4@later.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    browser.find_element_by_css_selector("#file").send_keys(file_path)
    browser.find_element_by_css_selector("body > div > form > button").click()
    
finally:

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    
    time.sleep(10)
    
    # закрываем браузер после всех манипуляций
    
    browser.quit()

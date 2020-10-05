from selenium import webdriver

import time


try: 
    
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)       
    browser.find_element_by_id("button")
	
finally:

    # ожидание чтобы визуально оценить результаты прохождени€ скрипта
    
    time.sleep(10)
    
    # закрываем браузер после всех манипул€ций
    
    browser.quit()

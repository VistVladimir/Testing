from selenium import webdriver

import time


try: 
    
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)    
    # Ваш код, который заполняет обязательные поля
    
    form1 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[1]/input")
	
    form1.send_keys("Leon")
	
    form2 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[2]/input")
	
    form2.send_keys("Kennedy")
	
    form3 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[3]/input")
    form3.send_keys("4@later.com")
    
    # Отправляем заполненную форму

    time.sleep(5)    
    browser.find_element_by_css_selector("body > div > form > button").click()
    
    # Проверяем, что смогли зарегистрироваться
    
    # ждем загрузки страницы
    
    time.sleep(5)
    
    # находим элемент, содержащий текст
    
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    
    welcome_text = welcome_text_elt.text
    
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    
    time.sleep(5)
    
    # закрываем браузер после всех манипуляций
    
    browser.quit()

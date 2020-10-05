from selenium import webdriver

import time


try: 
    
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)    
    # ��� ���, ������� ��������� ������������ ����
    
    form1 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[1]/input")
	
    form1.send_keys("Leon")
	
    form2 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[2]/input")
	
    form2.send_keys("Kennedy")
	
    form3 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[3]/input")
    form3.send_keys("4@later.com")
    
    # ���������� ����������� �����

    time.sleep(5)    
    browser.find_element_by_css_selector("body > div > form > button").click()
    
    # ���������, ��� ������ ������������������
    
    # ���� �������� ��������
    
    time.sleep(5)
    
    # ������� �������, ���������� �����
    
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    
    # ���������� � ���������� welcome_text ����� �� �������� welcome_text_elt
    
    welcome_text = welcome_text_elt.text
    
    # � ������� assert ���������, ��� ��������� ����� ��������� � ������� �� �������� �����
    
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:

    # �������� ����� ��������� ������� ���������� ����������� �������
    
    time.sleep(5)
    
    # ��������� ������� ����� ���� �����������
    
    browser.quit()

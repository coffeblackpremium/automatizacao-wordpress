from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



def efetuar_login(driver):
    try:
        login = driver.find_element_by_id('user_login')
        password = driver.find_element_by_id("user_pass")
        login_submit = driver.find_element_by_id("wp-submit")
        
        password.send_keys("pro80of")
        login.send_keys("producao")
        login_submit.click()
        time.sleep(5)
    except:
        #Tratar futuros excepts
        pass

def listas_de_posts(driver):
    html_source = Element.getAttribute('innerHtml')


    try:
        pass
    except:
        pass



PATH = "C:\chromedriver.exe" #Altere está linha para o Chrome Driver

lists = []

driver = webdriver.Chrome(PATH)
print(driver.title)
driver.get("http://obrasflex.com.br/wp-admin/edit.php?post_type=listing")
efetuar_login(driver=driver)
source_html = driver.page_source
print(source_html)

time.sleep(30)


#driver.get("https://obrasflex.com.br/wp-admin")
#efetuar_login(driver=driver)





time.sleep(5)
driver.quit()
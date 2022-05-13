from asyncio.windows_events import NULL
from distutils.command.build import build
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import win32clipboard

def efetuar_login(driver):
    try:
        login = driver.find_element(By.ID, 'user_login').send_keys("producao")
        password = driver.find_element(By.ID, "user_pass").send_keys("pro80of")
        login_submit = driver.find_element(By.ID, "wp-submit").click()
        time.sleep(5)
    except:
        #Tratar futuros excepts
        pass

def add_tags(driver):
    title = driver.find_elements(By.XPATH, "//input[@class='ptitle']")
    get_tag = driver.find_element(By.XPATH, "//textarea[@class='tax_input_list-tags ui-autocomplete-input']")
    button_atualizar = driver.find_elements(By.XPATH, "//button[@class='button button-primary save alignright']")[0]
    get_title = title[0]
    if get_title:
        get_title.send_keys(Keys.CONTROL, 'a')
        get_title.send_keys(Keys.CONTROL, 'c')
        win32clipboard.OpenClipboard()
        text = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        time.sleep(2)
        get_tag.send_keys(Keys.CONTROL, 'v')
        button_atualizar.click()
        
PATH = "C:\chromedriver.exe" #Altere está linha para o Chrome Driver

driver = webdriver.Chrome(PATH)
print(driver.title)
driver.get("http://obrasflex.com.br/wp-admin/edit.php?post_type=listing")
efetuar_login(driver=driver)
posts = driver.find_elements(By.XPATH, "//button[@class='button-link editinline']")
#posts = WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//button[@class='button-link editinline']")))
#text = WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located((By.XPATH, "//a[@class='row-title']")))
text = driver.find_elements(By.XPATH, "//a[@class='row-title']")
for count in range(0, 600):
    post_counts = posts[count]
    if post_counts:
        click_posting = posts[count]
        hover = ActionChains(driver).move_to_element(text[count]).perform()
        driver.implicitly_wait(10)
        click_posting.click()
        add_tags(driver=driver)
        time.sleep(5)
time.sleep(30)


#driver.get("https://obrasflex.com.br/wp-admin")
#efetuar_login(driver=driver)

time.sleep(5)
driver.quit()
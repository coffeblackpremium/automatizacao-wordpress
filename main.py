from asyncio.windows_events import NULL
from distutils.command.build import build
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import win32clipboard

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
"""
def copy_text_for_clipboard(driver):
    driver.send_keys(Keys.CONTROL, 'a')
    driver.send_keys(Keys.CONTROL, 'c')
    win32clipboard.OpenClipboard()
    text = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return text
"""
def add_tags(driver):
    title = driver.find_elements_by_xpath("//input[@class='ptitle']")
    get_tag = driver.find_element_by_xpath("//textarea[@class='tax_input_list-tags ui-autocomplete-input']")
    button_atualizar = driver.find_elements_by_xpath("//button[@class='button button-primary save alignright']")[0]
    get_title = title[0]
    if get_title:
        get_title.send_keys(Keys.CONTROL, 'a')
        get_title.send_keys(Keys.CONTROL, 'c')
        win32clipboard.OpenClipboard()
        text = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        get_tag.send_keys(Keys.CONTROL, 'v')
        button_atualizar.click()
        
PATH = "C:\chromedriver.exe" #Altere está linha para o Chrome Driver

driver = webdriver.Chrome(PATH)
print(driver.title)
driver.get("http://obrasflex.com.br/wp-admin/edit.php?post_type=listing")
efetuar_login(driver=driver)
source_html = driver.page_source
posts = []
posts = driver.find_elements_by_xpath("//button[@class='button-link editinline']")

for count in range(0, 600):
    post_counts = posts[count]
    if post_counts:
        click_posting = post_counts
        driver.implicitly_wait(10)
        click_posting.click()
        add_tags(driver=driver)
        time.sleep(5)
time.sleep(30)


#driver.get("https://obrasflex.com.br/wp-admin")
#efetuar_login(driver=driver)

time.sleep(5)
driver.quit()
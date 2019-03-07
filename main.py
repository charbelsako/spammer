# a selenium whatsapp spammer
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# config variables and/or constants
from config import *

driver = webdriver.Firefox(firefox_profile=PROFILE)
driver.get(URL)
# make the driver wait before querying for objects
try:
    wait = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, '_1wjpf'))      
    )
except:
    print('oops')

# navigate to the contact
# contact = driver.find_element_by_class_name('_1wjpf')
# print(contact)
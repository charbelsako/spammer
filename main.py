# a selenium whatsapp spammer
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pyautogui import typewrite, hotkey

# config variables and/or constants
from config import *

driver = webdriver.Firefox(firefox_profile=PROFILE)
driver.get(URL)
# make the driver wait before querying for objects
try:
    wait = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, CONTACT_CLASS_NAME))      
    )
except:
    print('oops')

# WIP: Refactor this code. use find_elements. and choose the one you want.
# navigate to the contact

# all the contacts
contacts = driver.find_elements_by_class_name(CONTACT_CLASS_NAME)

spans = [c.find_elements_by_xpath('.//span') for c in contacts]

names = []
for i in range(len(spans)):
    if len(spans[i]) > 1:
        names.append(spans[i][1].get_attribute("title"))
    else:
        names.append(spans[i][0].get_attribute("title"))


def remove_space(x):
    return x.replace(" ", "")

names = list(map(remove_space, names))
# names = [n.split() for n in names if len(n) > 0]
# print(names)
# names = [''.join([n[0], n[1]]) for n in names if len(n) > 1]
print(names)
index = names.index(CONTACT_NAME)
contact = contacts[index]
contact.click()

# send the contact random text messages
for i in range(NUM_MSGS):
    typewrite('quick brown fox')
    send = driver.find_element_by_class_name(SEND_BUTTON_CLASS)
    send.click()

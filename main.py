# a selenium whatsapp spammer
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pyautogui import typewrite
from time import sleep

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

# navigate to the contact and click on the div
contacts = driver.find_elements_by_class_name(CONTACT_CLASS_NAME)
print("You have {} contacts.\n".format(len(contacts)))
spans = [c.find_elements_by_xpath('.//span') for c in contacts]

names = []
for i in range(len(spans)):
    if len(spans[i]) > 1:
        names.append(spans[i][1].get_attribute("title"))
    else:
        names.append(spans[i][0].get_attribute("title"))
# debugging
print("With {} names.\n".format(len(names)))

def remove_space(x):
    return x.replace(" ", "")

names = list(map(remove_space, names))
print(names)
index = names.index(CONTACT_NAME)
contact = contacts[index]
contact.click()

# send the contact random text messages or predefined text
for i in range(NUM_MSGS):
    if not USE_RANDOM_TEXT:
        if SEND_WHOLE_MESSAGE:
            typewrite(MESSAGES)
        else:
            typewrite(MESSAGES[i%len(MESSAGES)])
    else:
        typewrite('quick brown fox')
    sleep(1)
    send = driver.find_element_by_class_name(SEND_BUTTON_CLASS)
    send.click()

# change these variables where needed
CONTACT_NAME = 'Melissa'
# number of messages to send to the contact
NUM_MSGS = 10
# if set to False, send these messages instead of random text
# not implemented yet
# TODO: refactor
USE_RANDOM_TEXT = True
MESSAGES = ['USER', 'DEFINED', 'MESSAGES']
# the browser that you use
BROWSER_NAME = 'Firefox'

# browser info
# the profile allows the app to keep the user logged in and use previously opened sessions.
CHROME_DATA_DIR = ''
# change to your directory
FIREFOX_PROFILE = '/home/charbelsako/.mozilla/firefox/'
# change to your profile name
PROFILE_NAME = 'm2y35oha.default'

if BROWSER_NAME == 'Chrome'.lower():
    PROFILE = CHROME_DATA_DIR
else:
    PROFILE = ''.join([FIREFOX_PROFILE, PROFILE_NAME])

URL = "https://web.whatsapp.com"
# the contact card that you can click on
CONTACT_CLASS_NAME = "_3j7s9"
# contact name class. Could be obsolete
CONTACT_NAME_CLASS = "_1wjpf"
SEND_BUTTON_CLASS = "_35EW6"
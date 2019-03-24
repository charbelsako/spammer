# change these variables where needed
CONTACT_NAME = 'Simon Daccache'
NUM_MSGS = 3000000000
# if set to False, send these messages instead of random text
USE_RANDOM_TEXT = False
SEND_WHOLE_MESSAGE = False
MESSAGE = 'USER DEFINED MESSAGE'
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
SEND_BUTTON_CLASS = "_35EW6"

CONTACT_NAME = CONTACT_NAME.replace(" ", "")
if not SEND_WHOLE_MESSAGE:
    MESSAGES = MESSAGE.split()
else:
    MESSAGES = MESSAGE

# change these variables where needed
URL = 'https://web.whatsapp.com'

# browser info
BROWSER_NAME = 'Firefox'
# the profile allows the app to keep the user logged and use previously opened sessions.
CHROME_DATA_DIR = ''
FIREFOX_PROFILE = '/home/charbelsako/.mozilla/firefox/'
PROFILE_NAME = 'm2y35oha.default'

if BROWSER_NAME == 'Chrome'.lower():
    PROFILE = CHROME_DATA_DIR
else:
    PROFILE = ''.join([FIREFOX_PROFILE, PROFILE_NAME])

CONTACT_NAME = 'Markos Emile'
# number of messages to send to the contact
NUM_MSGS = 0 

# if set to True send these messages instead of random text
USE_RANDOM_TEXT = False
MESSAGES = ['USER', 'DEFINED', 'MESSAGES']


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

CONTACT_NAME = 'Markos'
# number of messages to send to the contact
NUM_MSGS = 0 

# if set to True send these messages instead of random text
USE_RANDOM_TEXT = False
MESSAGES = ['USER', 'DEFINED', 'MESSAGES']

# the activator has to have a class of focused so you can type your message
ACTIVATOR_CLASS_NAME = '_3F6QL'
# the input field. although this is a div
INPUT_CLASS_NAME = '_2S1VP'
# the contact card that you can click on
CONTACT_CLASS_NAME = '_3j7s9'
# contact name class
CONTACT_NAME_CLASS = '_1wjpf'
CONTACT_NAME_PARENT_CLASS = '_3TEwt'

SEND_BUTTON_CLASS = "_35EW6"
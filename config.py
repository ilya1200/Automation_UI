import os
from pathlib import Path

TIME_TO_WAIT = 20
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CHROME_DRIVER_PATH = str(Path(f'{ROOT_DIR}//drivers/chromedriver.exe'))

# Page URLs
AUTOMATION_TESTING_PAGE_URL = "http://demo.automationtesting.in/"
REGISTER_PAGE_URL = "http://demo.automationtesting.in/Register.html"
WEB_TABLE_PAGE_URL = 'http://demo.automationtesting.in/WebTable.html'
FRAMES_PAGE_URL = "http://demo.automationtesting.in/Frames.html"
ALERTS_PAGE_URL = "http://demo.automationtesting.in/Alerts.html"

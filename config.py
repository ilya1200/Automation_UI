import os
from pathlib import Path

TIME_TO_WAIT = 20
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CHROME_DRIVER_PATH = str(Path(f'{ROOT_DIR}//drivers/chromedriver.exe'))

# Page URLs
TECHDEMO_PAGE_URL = "https://techdemotbaseo.kinsta.cloud/"
TECHDEMO_ABOUT_PAGE_URL = "https://techdemotbaseo.kinsta.cloud/about-us/"

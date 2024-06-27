import os
from dotenv import load_dotenv

load_dotenv()

BROWSER_TYPES = {
    1: 'chrome',
    2: 'firefox',
    3: 'edge',
}

DEVICE_TYPES = {
    'm': 'mobile',
    'd': 'desktop'
}

BROWSER = int(os.getenv('BROWSER', 1))
DEVICE = os.getenv('DEVICE', 'm')
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
LOGIN_URL = os.getenv("LOGIN_URL")
REWARDS_URL = os.getenv("REWARDS_URL")
BING_URL = os.getenv("BING_URL")
RANDOMWORDS_API_URL = os.getenv("RANDOMWORDS_API")
DRIVER_PATH_CHROME = os.getenv("DRIVER_PATH_CHROME")
DRIVER_PATH_FIREFOX = os.getenv("DRIVER_PATH_FIREFOX")
DRIVER_PATH_EDGE = os.getenv("DRIVER_PATH_EDGE")
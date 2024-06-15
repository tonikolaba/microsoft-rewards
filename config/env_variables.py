import os
from dotenv import load_dotenv, find_dotenv
# loading variables from .env file
dotenv_path = find_dotenv()

load_dotenv(dotenv_path) 
 
class Config:
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")
    LOGIN_URL = os.getenv("LOGIN_URL")
    BING_URL = os.getenv("BING_URL")

config = Config()

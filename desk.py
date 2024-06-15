from config import env_variables
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests, re, time

class BingSearchBot:
    def __init__(self, email, password, login_url, bing_url):
        self.email = email
        self.password = password
        self.login_url = login_url
        self.bing_url = bing_url
        self.browser = webdriver.Chrome()
        
    def login_to_microsoft_account(self):
        self.browser.get(self.login_url)
        
        # Find and input email
        email_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "i0116"))
        )
        email_input.send_keys(self.email)
        # Wait for login button to become clickable
        login_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.ID, "idSIButton9"))
        )
        # Click login button
        login_button.click()

       # choose other way, not MFA
        login_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.ID, "idA_PWD_SwitchToCredPicker"))
        )

        # Click login button
        login_button.click()
        print("moment ot select the Not MFA")
        # Wait for the login button to become clickable
        login_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='tileList']/div/div/button/div[2]/div"))
        )
        login_button.click()

        print("Please Enter your localy password??? ")
        time.sleep(10)

        print("Stay singed in? ")
        # O = id: declineButton 1 = id : acceptButton
        login_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.ID, "declineButton"))
        )

        #Click login button
        login_button.click()

        time.sleep(10)

         # Open Bing
        self.browser.get(self.bing_url)

        print("Start search on Bing automaticly")
        # Define a function to get random words from API
        def get_random_words():
            response = requests.get('https://random-word-api.herokuapp.com/word?number=3')
            return response.json()

        for i in range(90):
            # Get random words from API
            random_words = get_random_words()
            search_word = ""
            for word in random_words:
                # Add regex pattern to each word
                regex_word = re.sub(r'([.*+?^${}()|\[\]\/\\])', r'\\\1', word)
                search_word += regex_word + " "

            # Find the search input field
            search_input = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.NAME, "q"))
            )

            # Clear the search input field
            search_input.clear()

            # Enter the random word to search for
            search_input.send_keys(search_word)

            # Submit the search query
            search_input.submit()

            # Wait for 2 seconds before the next search
            time.sleep(8)



    def run(self):
        self.login_to_microsoft_account()
        # Keep the browser open after login
        input("Press any key to close the browser...")
        # Since we want to keep the browser open, we don't call browser.quit() here

# Load environment variables from .env file
email = env_variables.config.EMAIL
password = env_variables.config.PASSWORD
login_url = env_variables.config.LOGIN_URL
bing_url = env_variables.config.BING_URL
bing_bot = BingSearchBot(email, password, login_url, bing_url)

bing_bot.run()

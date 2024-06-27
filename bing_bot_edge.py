from driver_manager import WebDriverConf
from wonderwords import RandomWord
from config.config import BROWSER, DEVICE, EMAIL, PASSWORD , LOGIN_URL, BING_URL, RANDOMWORDS_API_URL , REWARDS_URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests, re, time

class BingSearchBot:
    def __init__(self, email, password, rewards_url, bing_url):
        self.email = email
        self.password = password
        self.rewards_url = rewards_url
        self.bing_url = bing_url
        self.randomwords_api_url = randomwords_api_url
        self.browser = None

    def login_to_microsoft_account(self):
        try:
            self.browser.get(self.rewards_url)
           
            print("Please Enter your localy password MANUALY??? ")
            time.sleep(10)
        except Exception as e:
            print(f"Error logging in: {e}")

        # Open Bing
        self.browser.get(self.bing_url)

    def search_on_bing(self):
        print("Start Search on Bing automatically")

        # Define a function to get random words
        get_random_words = RandomWord()

        for i in range(90):
            # Get random words
            random_words =  get_random_words.random_words(3)
            search_word = ""

            for word in random_words:
                # Add regex pattern to each word
                regex_word = re.sub(r'([.*+?^${}()|\[\]\/\\])', r'\\\1', word)
                search_word += regex_word + " "

            # Find the search input field
            try:
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
                time.sleep(7)
            except Exception as e:
                print(f"Error searching: {e}")

    def run(self):
        wd = WebDriverConf(BROWSER, DEVICE)
        self.browser = wd.get_driver()
        self.login_to_microsoft_account()
        self.search_on_bing()
        self.browser.quit

if __name__ == "__main__":
    # Load environment variables from .env file
    email = EMAIL
    password = PASSWORD
    login_url = LOGIN_URL
    rewards_url = REWARDS_URL
    bing_url = BING_URL
    randomwords_api_url = RANDOMWORDS_API_URL
    bing_bot = BingSearchBot(email, password, rewards_url, bing_url)
    bing_bot.run()
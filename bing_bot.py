from driver_manager import WebDriverConf
from config.config import BROWSER, DEVICE, EMAIL, PASSWORD , LOGIN_URL, BING_URL, RANDOMWORDS_API_URL 
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
        self.randomwords_api_url = randomwords_api_url
        self.browser = None

    def login_to_microsoft_account(self):
        try:
            self.browser.get(self.login_url)
            # Find and input email
            try:
                email_input = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.ID, "i0116"))
                )
                email_input.send_keys(self.email)
                email_input.click()

                # Wait for login button to become clickable
                login_button = WebDriverWait(self.browser, 10).until(
                    EC.element_to_be_clickable((By.ID, "idSIButton9"))
                )
                # Click login button
                login_button.click()
            except Exception as e:
                print(f"Error logging in: {e}")
                return
            
            #Find and input password
            '''
            try:
                password_input = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.ID, "i0118"))
                )

                password_input.send_keys(self.password)
                password_input.click()

                # Wait for login button to become clickable
                login_button = WebDriverWait(self.browser, 10).until(
                    EC.element_to_be_clickable((By.ID, "idSIButton9"))
                )
                # Click login button
                login_button.click()
            except Exception as e:
                print(f"Error logging in: {e}")
                return
            '''
            # Choose other way, not MFA
            try:
                login_button = WebDriverWait(self.browser, 10).until(
                    EC.element_to_be_clickable((By.ID, "idA_PWD_SwitchToCredPicker"))
                )
                login_button.click()

            except Exception as e:
                print(f"Error choosing other way: {e}")
                return
            try:
                elements = WebDriverWait(self.browser, 10).until(
                  EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".___b9iavz0.f10pi13n.f17n1hoa"))
                )
                elements[0].click()

            except Exception as e:
                print(f"Error choosing other way: {e}")
                return

            print("Please Enter your localy password MANUALY??? ")
            time.sleep(10)

            print("Stay singed in? ")
            # O = id: declineButton 1 = id : acceptButton
            try:
                login_button = WebDriverWait(self.browser, 10).until(
                    EC.element_to_be_clickable((By.ID, "acceptButton"))
                )
                login_button.click()
            except Exception as e:
                print(f"Error staying signed in: {e}")
                return
        except Exception as e:
            print(f"Error logging in: {e}")

    def search_on_bing(self):
        print("Start Search on Bing automatically")
        # Open Bing
        self.browser.get(self.bing_url)
        # Define a function to get random words from API
        def get_random_words():
            response = requests.get(randomwords_api_url)
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
    bing_url = BING_URL
    randomwords_api_url = RANDOMWORDS_API_URL
    bing_bot = BingSearchBot(email, password, login_url, bing_url)
    bing_bot.run()
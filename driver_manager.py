from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

class WebDriverConf:
    def __init__(self, driver_choice, device):
        self.driver_choice = driver_choice
        self.device = device

    def get_driver(self):
        if self.driver_choice == 1:  # Chrome
            service = ChromeService(ChromeDriverManager().install())
            options = ChromeOptions()
            if self.device == 'm':
                options.add_argument("--disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_argument("--disable-gpu")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--window-size=360,812")
                options.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone X'})
                return webdriver.Chrome(service=service, options=options)
            elif self.device == 'd':
                return webdriver.Chrome(service=service, options=None)
        elif self.driver_choice == 2:  # Firefox
            service = FirefoxService(GeckoDriverManager().install())
            service.log_output = None
            options = FirefoxOptions()
            options.add_argument("--window-size=360,812")
            if self.device == 'm':
                options.set_preference("general.useragent.override", "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Mobile/14A345 Safari/604.1")
                options.set_preference("network.proxy.type", 1)
                options.set_preference("network.proxy.http", "proxy.com")
                options.set_preference("network.proxy.http_port", 8080)
                return webdriver.Firefox(service=service, options=options)
            elif self.device == 'd':
                return webdriver.Firefox(service=service, options=None)
        elif self.driver_choice == 3:  # Edge
            service = EdgeService(EdgeChromiumDriverManager().install())
            options = EdgeOptions()
            options.add_argument("--ignore-certificate-errors")
            options.add_argument("--ignore-ssl-errors")
            if self.device == 'm':
                options.add_argument("--disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_argument("--disable-gpu")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--window-size=360,812")
                options.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone X'})
                return webdriver.Edge(service=service, options=options)
            elif self.device == 'd':
                return webdriver.Edge(service=service, options=None)
        else:
            raise ValueError("Invalid browser choice")
   


if __name__ == "__main__":
    print("This is driver manager file. Don't run this file directly.")
<p align="center">
  <a href="https://rewards.bing.com/welcome" target="blank"><img src="https://az15297.vo.msecnd.net/images/rewards/membercenter/missions/Ms_Logo_48px.png" width="48" alt="Microsoft Rewards" />
  </a>
</p>

<p align="center">
<a href="https://rewards.bing.com/welcome"><img src="https://img.shields.io/badge/Website-Microsoft%20Rewards-19aaa3" alt="Microsoft Rewards Website"></a>
</p>

<p align="center">
<a href="https://www.google.com/chrome/"><img src="https://img.shields.io/badge/Google%20Chrome%20-Test-brightgreen" alt="Chrome Browser">
<a href="https://www.mozilla.org/en-US/firefox/new/"><img src="https://img.shields.io/badge/Mozilla%20Firefox%20-Test-yellow" alt="Firefox Browser">
<a href="https://www.microsoft.com/en-us/edge/download?form=MA13FJ"><img src="https://img.shields.io/badge/Microsoft%20Edge%20-Test-yellow" alt="Edge Browser">
<img alt="Python" src="https://img.shields.io/badge/Python%20-3.7.4-brightgreen">
<img alt="pip" src="https://img.shields.io/badge/pip%20-24.0-brightgreen">
<img alt="Selemium" src="https://img.shields.io/badge/Selenium%20-4.11.2-brightgreen">
</a>
</p>


# Microsoft Rewards :medal_sports: Automation Tests

A project created in Python-based automation script using Selenium to automate the process of earning Microsoft Rewards points through targeted searches, thereby boosting rewards balance.


## Run :technologist::bulb:

- Create an `.env` file & add all data as in the example file `.env.example`, set data as you need.
- Make sure you're using the same tools and version settings as we have tested
- For the moment, it is the test for MFA Microsoft accounts, and need to manually add the password of your PC, for users with just email & password need to uncomment the code.

- run by type `python .\bing_bot.py` when `.\bing_bot.py` name file.

:warning:
```sh
-> Update browser drivers. 
-> Use Edge for accessibility.
-> When using the mobile version, choose to inspect and manually set the mobile view. 
-> Clear browsing history and cache.
```

- May not need to install

```
 pip install python-dotenv 
 pip install webdriver-manager 
 pip install selenium 
 pip install msedgedriver
 pip install selenium-wire
```


#### Browser Settings


| Device        | Browser Choice |     Check   |
| ------------- |----------------|-------------|
| `m` (Mobile)  | `1`  Chrome    | :white_check_mark: |
|               | `2`  Firefox   | :warning: |
|               | `3`  Edge      | :warning: |
| `d` (Desktop) | `1`  Chrome    | :white_check_mark: |
|               | `2`  Firefox   | :warning: |
|               | `3`  Edge      | :warning: |

To configure the browser settings, you can specify the device type and browser choice using the following options:

    m: Mobile device
    d: Desktop device

You can choose between the following browsers:

    1: Google Chrome
    2: Mozilla Firefox
    3: Microsoft Edge

#### Drivers Use 

| Browser | Manually Download | Automatically* | 
| ------- |----------------|----------------|
|Chrome   | `https://chromedriver.chromium.org/downloads` | `ChromeService(ChromeDriverManager().install())` |
|Firefox  | `https://github.com/mozilla/geckodriver/releases` |`FirefoxService(GeckoDriverManager().install())`  |
|Edge     | `https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/` | `EdgeService(EdgeChromiumDriverManager().install())` |

* On the `driver_manager.py` file, you need to change the `service` to respective values and make sure to be imported and keep browsers updated.

### Developed

<p align="center">
  <a href="https://www.linkedin.com/company/kolabashpk" target="blank"><img src="https://s6.imgcdn.dev/R7jxC.png" width="390" alt="Kolaba logo" /></a>
</p>
<p align="center">
with ❤️ by: <a href="https://github.com/tonikolaba" target="blank">nkolaba</a> ©️
</p>

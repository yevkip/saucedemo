import logging
import os
from selenium import webdriver

# Configure logging
logging.basicConfig(level=logging.INFO)


def get_driver(config, browser_name):
    local_browsers = {'Firefox': webdriver.Firefox,
                      'Chrome': webdriver.Chrome}

    remote_browsers = {'Firefox': webdriver.FirefoxOptions(),
                       'Chrome': webdriver.ChromeOptions()}

    browser_config = config['browsers'].get(browser_name)
    browser = browser_config['browser']

    if browser_config['type'] == 'local':
        driver = local_browsers.get(browser)
        return driver()

    elif browser_config['type'] == 'remote':
        driver = remote_browsers.get(browser)
        grid_url = browser_config.get('grid_url')
        driver.add_argument('--headless')

        return webdriver.Remote(command_executor=grid_url, options=driver)

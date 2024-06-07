import logging
import os
from selenium import webdriver


# Configure logging
logging.basicConfig(level=logging.INFO)


def get_driver(config, browser_name):
    local_browsers = {
        'Firefox': webdriver.Firefox,
        'Chrome': webdriver.Chrome
    }

    remote_browsers = {
        'Firefox': webdriver.FirefoxOptions(),
        'Chrome': webdriver.ChromeOptions()
    }

    # Enable headless mode for remote browsers
    for browser, options in remote_browsers.items():
        options.add_argument('--headless')

    browser_config = config['browsers'].get(browser_name)

    if not browser_config:
        raise RuntimeError('Browser configuration not found')

    if browser_config['type'] == 'local':
        driver_class = local_browsers.get(browser_config['browser'])
        if driver_class:
            return driver_class()
        else:
            raise RuntimeError(f"Unsupported local browser: {browser_config['browser']}")

    elif browser_config['type'] == 'remote':
        grid_url = browser_config.get('grid_url')
        browser = browser_config.get('browser')
        options = remote_browsers.get(browser)

        if not grid_url or not options:
            raise RuntimeError('Grid URL or desired capabilities not specified for remote browser')

        return webdriver.Remote(command_executor=grid_url, options=options)

    else:
        raise RuntimeError('Unknown browser type')

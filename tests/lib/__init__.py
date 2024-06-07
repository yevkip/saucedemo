from .web_app import WebApp
from .driver import get_driver


def get_app(config, browser_name):
    driver = get_driver(config, browser_name)
    environment_config = config
    return WebApp(driver=driver,
                  environment_config=environment_config)


__all__ = ['get_app', 'WebApp']

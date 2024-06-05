from .web_app import WebApp
from .driver import get_driver


def get_app(config):
    driver = get_driver(config)
    environment_config = config
    return WebApp(driver, environment_config)


__all__ = ['get_app', 'WebApp']

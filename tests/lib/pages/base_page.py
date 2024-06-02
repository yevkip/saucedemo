from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    ready_selector = None

    def __init__(self, driver):
        self.d = driver

    def wait(self):
        WebDriverWait(self.d, 20).until(
            lambda driver:
            driver
                .find_element(*self.ready_selector))

    def is_active(self):
        assert self.d.find_element(*self.ready_selector).is_displayed()

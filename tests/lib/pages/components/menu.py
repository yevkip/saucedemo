import time

from selenium.webdriver.common.by import By

from tests.lib.pages.base_page import BasePage


class Menu(BasePage):
    logout_link_selector = 'logout_sidebar_link'

    def __init__(self, driver):
        super(Menu, self).__init__(driver)

    def logout(self):
        time.sleep(1)
        return self.d.find_element(By.ID, self.logout_link_selector).click()




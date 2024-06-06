from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    ready_selector = None
    menu_btn_selector = 'react-burger-menu-btn'

    def __init__(self, driver):
        self.d = driver

    def wait(self):
        WebDriverWait(self.d, 20).until(
            lambda driver:
            driver
                .find_element(*self.ready_selector))

    def is_active(self):
        assert self.d.find_element(*self.ready_selector).is_displayed()

    def open_menu(self):
        return self.d.find_element(By.ID, self.menu_btn_selector).click()

    def store_product_values(self, products):

        if type(products) == dict:
            return products
        else:
            pr_dict = {}
            for product in products:
                pr_dict[product.name] = {"description": product.description,
                                         "price": product.price}
            return pr_dict

from selenium.webdriver.common.by import By
from tests.lib.pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    def __init__(self, driver):
        super(CheckoutCompletePage, self).__init__(driver)

    ready_selector = ('xpath', '//span[contains(text(), "Checkout: Complete!")]')
    checkout_complete_selector = 'checkout_complete_container'
    checkout_complete_header_selector = 'complete-header'
    checkout_complete_icon = 'pony_express'

    def verify_checkout_complete(self):
        assert self.d.find_element(By.ID, self.checkout_complete_selector)
        assert self.d.find_element(By.CLASS_NAME, self.checkout_complete_icon)
        assert self.d.find_element(By.CLASS_NAME,
                                   self.checkout_complete_header_selector).text == 'Thank you for your order!'

from selenium.webdriver.common.by import By
from tests.lib.pages.base_page import BasePage

USER_FIRST_NAME = 'James'
USER_LAST_NAME = 'Bond'
USER_ZIP_CODE = '01234'


class CheckoutPage(BasePage):
    first_name_selector = 'first-name'
    last_name_selector = 'last-name'
    zip_code_selector = 'postal-code'
    continue_btn_selector = 'continue'

    def __init__(self, driver):
        super(CheckoutPage, self).__init__(driver)

    @property
    def first_name_input(self):
        return self.d.find_element(By.ID, self.first_name_selector)

    @property
    def last_name_input(self):
        return self.d.find_element(By.ID, self.last_name_selector)

    @property
    def zip_code_input(self):
        return self.d.find_element(By.ID, self.zip_code_selector)

    @property
    def continue_btn(self):
        return self.d.find_element(By.ID, self.continue_btn_selector)

    def complete_checkout_info(self, first_name=USER_FIRST_NAME, last_name=USER_LAST_NAME, zip=USER_ZIP_CODE):
        self.first_name_input.send_keys(first_name)
        self.last_name_input.send_keys(last_name)
        self.zip_code_input.send_keys(zip)

    def complete_checkout_info_and_submit(self, ):
        self.complete_checkout_info()
        self.continue_btn.click()


from selenium.webdriver.common.by import By
from tests.lib.pages.base_page import BasePage

USER_FIRST_NAME = 'James'
USER_LAST_NAME = 'Bond'
USER_ZIP_CODE = '01234'


class CheckoutPage(BasePage):
    ready_selector = ('xpath', '//span[contains(text(), "Checkout: Your Information")]')
    first_name_selector = 'first-name'
    last_name_selector = 'last-name'
    zip_code_selector = 'postal-code'
    continue_btn_selector = 'continue'
    checkout_data_error = 'error-message-container'

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

    def _input_value(self, value, _id):
        value = '' if value == '[blank]' else value
        input_field = self.d.find_element('id', _id)
        input_field.send_keys(value)

    def enter_first_name(self, first_name):
        self._input_value(first_name, self.first_name_selector)
        print(f'Enter {first_name} to first name field')

    def enter_last_name(self, last_name):
        self._input_value(last_name, self.last_name_selector)
        print(f'Enter {last_name} to last name field')

    def enter_zip(self, zip):
        self._input_value(zip, self.zip_code_selector)
        print(f'Enter {zip} to zip code field')

    def complete_checkout_info(self, first_name=USER_FIRST_NAME, last_name=USER_LAST_NAME, zip=USER_ZIP_CODE):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_zip(zip)

    def complete_checkout_info_and_submit(self, first_name=USER_FIRST_NAME, last_name=USER_LAST_NAME, zip=USER_ZIP_CODE):
        self.complete_checkout_info(first_name, last_name, zip)
        self.continue_btn.click()

    def verify_checkout_info_missed_error(self):
        assert 'Error' in self.d.find_element(By.CLASS_NAME, self.checkout_data_error).text



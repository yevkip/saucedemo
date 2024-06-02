from selenium.webdriver.common.by import By

from .base_page import BasePage


class LoginPage(BasePage):
    ready_selector = ('id', 'login-button')
    login_selector = "user-name"
    password_selector = "password"
    error_selector = "//h3[@data-test='error']"
    login_btn_selector = ready_selector

    def _input_value(self, value, _id):
        value = '' if value == '[blank]' else value
        input_field = self.d.find_element('id', _id)
        input_field.send_keys(value)

    def enter_username(self, username):
        self._input_value(username, self.login_selector)
        print(f'Enter {username} to username field')

    def enter_password(self, password):
        self._input_value(password, self.password_selector)
        print(f'Enter {password} to password field')

    def click_login_btn(self):
        self.d.find_element(*self.login_btn_selector).click()
        print('Click login btn')

    def check_error_msg(self, error_msg):
        assert self.d.find_element(By.XPATH, self.error_selector).text == error_msg, error_msg


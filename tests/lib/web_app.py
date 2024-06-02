from .pages import LoginPage, ProductsPage, CartPage


class WebApp:
    def __init__(self, driver, environment_config):
        self.config = environment_config
        self.driver = driver
        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)
        self.cart_page = CartPage(self.driver)

    def shutdown(self):
        self.driver.quit()

    def open_base_page(self):
        self.driver.get(self.config['url'])
        self.login_page.wait()

    def login(self, username, password):
        self.login_page.enter_username(username)
        self.login_page.enter_password(password)
        self.login_page.click_login_btn()
        self.products_page.wait()

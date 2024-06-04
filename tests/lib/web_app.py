from .pages import LoginPage, ProductsPage, CartPage, CheckoutPage, CheckoutOverviewPage, CheckoutCompletePage


class WebApp:
    def __init__(self, driver, environment_config):
        self.config = environment_config
        self.driver = driver
        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)
        self.checkout_overview_page = CheckoutOverviewPage(self.driver)
        self.checkout_complete_page = CheckoutCompletePage(self.driver)

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

    def verify_cart_empty(self):
        self.products_page.verify_cart_badge_qty()

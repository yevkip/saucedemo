from .pages import BasePage, LoginPage, ProductsPage, CartPage, CheckoutPage, CheckoutOverviewPage, CheckoutCompletePage, Menu


class WebApp:
    def __init__(self, driver, environment_config):
        self.config = environment_config
        self.driver = driver
        self.login_page = LoginPage(self.driver)
        self.base_page = BasePage(self.driver)
        self.products_page = ProductsPage(self.driver)
        self.menu = Menu(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)
        self.checkout_overview_page = CheckoutOverviewPage(self.driver)
        self.checkout_complete_page = CheckoutCompletePage(self.driver)

    def get_username(self, user):
        user = 'user1' if user == 'User' else user
        username = self.config['credentials']['username'].get(user.lower())
        return username

    @property
    def password(self):
        return self.config['credentials']['password']

    def shutdown(self):
        self.driver.quit()

    def open_base_page(self):
        self.driver.get(self.config['environments']['url'])
        self.login_page.wait()

    def login(self, user):
        username = self.get_username(user)
        self.login_page.enter_username(username)
        self.login_page.enter_password(self.password)
        self.login_page.click_login_btn()
        self.products_page.wait()

    def verify_cart_empty(self):
        self.products_page.verify_cart_badge_qty()

from .cart_page import CartPage
from .checkout_complete_page import CheckoutCompletePage
from .checkout_overview_page import CheckoutOverviewPage
from .login_page import LoginPage
from .checkout_page import CheckoutPage
from .products_page import ProductsPage

page_map = {
    'Products': 'products_page',
    'Cart': 'cart_page',
    'Checkout Overview': 'checkout_overview_page',
    'Checkout: Complete!': 'checkout_complete_page'

}

__all__ = ['LoginPage', 'ProductsPage', 'CartPage', 'CheckoutPage', 'CheckoutOverviewPage', 'CheckoutCompletePage']

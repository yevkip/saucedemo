from .cart_page import CartPage
from .login_page import LoginPage
from .products_page import ProductsPage

page_map = {
    'Products': 'products_page',
}

__all__ = ['LoginPage', 'ProductsPage', 'CartPage']

import random

from .base_page import BasePage
from tests.lib.pages.components.product import InventoryItem
from selenium.webdriver.common.by import By


class ProductsPage(BasePage):
    ready_selector = ('xpath', '//span[contains(text(), "Products")]')
    inventory_item_selector = 'inventory_item'
    cart_selector = 'shopping_cart_link'
    cart_badge_selector = 'shopping_cart_badge'

    def __init__(self, driver):
        super(ProductsPage, self).__init__(driver)
        self.__cart = []
        self.products_in_cart = None

    @property
    def inventory_items(self):
        inventory_elements = self.d.find_elements(By.CLASS_NAME, self.inventory_item_selector)
        return [InventoryItem(item) for item in inventory_elements]

    @property
    def cart_badge_qty(self):
        return self.d.find_element(By.CLASS_NAME, self.cart_selector).text

    def navigate_to_cart(self):
        self.d.find_element(By.CLASS_NAME, self.cart_selector).click()

    def add_product(self, num=1, exclude_products=False):
        inventory_items = self.inventory_items
        idxs = random.sample(range(0, len(inventory_items)), int(num))

        for idx in idxs:
            inventory_item = inventory_items[idx]
            if inventory_item.action_btn.text == 'Add to cart':
                inventory_item.action_btn.click()
            else:
                raise Exception(f'{inventory_item.name} is already in cart. Not expected.')
            self.__cart.append(inventory_item)

    def remove_product(self, num=1):
        idxs = random.sample(range(0, len(self.__cart)), int(num))

        for idx in idxs:
            inventory_item = self.__cart[idx]
            if inventory_item.action_btn.text == 'Remove':
                inventory_item.action_btn.click()
            else:
                raise Exception(f'{inventory_item.name} is not in cart. Not expected.')
            self.__cart.remove(inventory_item)

    def update_cart(self, update_with=None):
        if update_with:
            for name in update_with:
                self.products_in_cart.pop(name)

        else:

            products_in_cart = {}
            for product in self.__cart:
                products_in_cart[product.name] = {}
                products_in_cart[product.name]['price'] = product.price
                # if product.descriprion:
                #     products_in_cart[product.name]['description'] = product.descriprion
            self.products_in_cart = products_in_cart

    def verify_cart_badge_qty(self, num):
        assert int(self.cart_badge_qty) == int(num)






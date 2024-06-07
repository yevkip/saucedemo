import random

from .base_page import BasePage
from tests.lib.pages.components.product import CartInventoryItem
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    ready_selector = ('xpath', '//span[contains(text(), "Your Cart")]')
    cart_item_selector = 'cart_item'
    cart_selector = 'shopping_cart_link'
    checkout_btn_selector = 'checkout_button'

    def __init__(self, driver):
        super(CartPage, self).__init__(driver)

    @property
    def cart_inventory_items(self):
        inventory_elements = self.d.find_elements(By.CLASS_NAME, self.cart_item_selector)
        return [CartInventoryItem(item) for item in inventory_elements]

    def proceed_to_checkout(self):
        self.d.find_element(By.CLASS_NAME, self.checkout_btn_selector).click()

    def verify_cart_items(self, expected_items):
        cart_inventory_items = self.cart_inventory_items
        assert len(cart_inventory_items) == len(
            expected_items), f'Actual items in cart {len(cart_inventory_items)}, Expected {len(expected_items)}'
        if expected_items:
            for item in cart_inventory_items:
                assert item.name in expected_items
                assert item.price == expected_items[item.name]['price']

    def remove_product(self, num=1):
        removed_products = []

        idxs = random.sample(range(0, len(self.cart_inventory_items)), int(num))

        for idx in idxs:
            inventory_item = self.cart_inventory_items[idx]
            if inventory_item.action_btn.text == 'Remove':
                item_name = inventory_item.name
                inventory_item.action_btn.click()
                removed_products.append(item_name)
            else:
                raise Exception(f'{inventory_item.name} is not in cart. Not expected.')

        return self.cart_inventory_items

    def verify_empty_cart_error(self):
        pass

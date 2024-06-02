import random

from .base_page import BasePage
from tests.lib.pages.components.product import InventoryItem, CartInventoryItem
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    ready_selector = ('xpath', '//span[contains(text(), "Your Cart")]')
    cart_item_selector = 'cart_item'
    cart_selector = 'shopping_cart_link'

    def __init__(self, driver):
        super(CartPage, self).__init__(driver)

    @property
    def cart_inventory_items(self):
        inventory_elements = self.d.find_elements(By.CLASS_NAME, self.cart_item_selector)
        return [CartInventoryItem(item) for item in inventory_elements]

    def verify_cart_items(self, expected_items):
        cart_inventory_items = self.cart_inventory_items
        assert len(cart_inventory_items) == len(expected_items)
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

        return removed_products




    # def add_product(self, num=1):
    #     idxs = set()
    #     inventory_items = self.inventory_items
    #
    #     while len(idxs) < num:
    #         idx = random.randint(0, len(inventory_items))
    #         if idx not in idxs:
    #             idxs.add(idx)
    #
    #     for idx in idxs:
    #         inventory_item = inventory_items[idx]
    #         inventory_item.action_btn.click()
    #         self.__cart.append(inventory_item)

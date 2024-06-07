from selenium.webdriver.common.by import By
from tests.lib.pages.base_page import BasePage
from tests.lib.pages.components.product import CheckoutOverviewInventoryItem
import re


class CheckoutOverviewPage(BasePage):
    def __init__(self, driver):
        super(CheckoutOverviewPage, self).__init__(driver)
        self.items_total_price = None

    ready_selector = ('xpath', '//span[contains(text(), "Checkout: Overview")]')
    checkout_overview_inventory_item_selector = 'cart_item'
    items_price_selector = 'summary_subtotal_label'
    tax_price_selector = 'summary_tax_label'
    summary_total_price_selector = 'summary_total_label'
    finish_checkout_btn_selector = 'finish'

    @property
    def summary_items_price(self):
        items_price_text = self.d.find_element(By.CLASS_NAME, self.items_price_selector).text
        items_price = float(re.findall("\d+\.\d+", items_price_text)[0])
        return items_price

    @property
    def summary_tax_price(self):
        tax_price_text = self.d.find_element(By.CLASS_NAME, self.tax_price_selector).text
        tax_price = float(re.findall("\d+\.\d+", tax_price_text)[0])
        return tax_price

    @property
    def summary_total_price(self):
        summary_total_price_text = self.d.find_element(By.CLASS_NAME, self.summary_total_price_selector).text
        summary_total_price = float(re.findall("\d+\.\d+", summary_total_price_text)[0])
        return summary_total_price

    @property
    def checkout_overview_inventory_items(self):
        inventory_elements = self.d.find_elements(By.CLASS_NAME, self.checkout_overview_inventory_item_selector)
        return [CheckoutOverviewInventoryItem(item) for item in inventory_elements]

    def verify_checkout_overview_inventory_items(self, expected_items):
        cart_inventory_items = self.checkout_overview_inventory_items
        assert len(cart_inventory_items) == len(expected_items)

        items_total_price = 0
        for item in cart_inventory_items:
            assert item.name in expected_items
            assert item.price == expected_items[item.name]['price']
            items_total_price += float(re.findall("\d+\.\d+", item.price)[0])

        self.items_total_price = items_total_price

    def verify_checkout_overview_total_price(self, expected_items_total_price):
        assert expected_items_total_price == self.summary_items_price
        expected_tax = round(expected_items_total_price * 0.08, 2)
        assert expected_tax == self.summary_tax_price
        assert expected_items_total_price + expected_tax == self.summary_total_price, print(
            f'Expected {expected_items_total_price + expected_tax}, Actual {self.summary_total_price}')

    def finish_checkout(self):
        self.d.find_element(By.ID, self.finish_checkout_btn_selector).click()

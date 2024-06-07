from selenium.webdriver.common.by import By


class ContextInventoryItem:
    def __init__(self, inventory_item):
        self.name = inventory_item.name
        self.price = inventory_item.price
        self.description = inventory_item.description


class InventoryItem:
    def __init__(self, element):
        self.element = element

    @property
    def name(self):
        return self.element.find_element(By.CLASS_NAME, 'inventory_item_name').text

    @property
    def description(self):
        return self.element.find_element(By.CLASS_NAME, 'inventory_item_desc').text

    @property
    def price(self):
        return self.element.find_element(By.CLASS_NAME, 'inventory_item_price').text

    @property
    def action_btn(self):
        return self.element.find_element(By.CLASS_NAME, 'btn_inventory')

    @property
    def in_cart(self):
        return True if self.action_btn.text == 'Remove' else False


class CartInventoryItem:
    def __init__(self, element):
        self.element = element

    @property
    def name(self):
        return self.element.find_element(By.CLASS_NAME, 'inventory_item_name').text

    @property
    def description(self):
        return self.element.find_element(By.CLASS_NAME, 'inventory_item_desc').text

    @property
    def price(self):
        return self.element.find_element(By.CLASS_NAME, 'inventory_item_price').text

    @property
    def action_btn(self):
        return self.element.find_element(By.CLASS_NAME, 'cart_button')


class CheckoutOverviewInventoryItem:
    def __init__(self, element):
        self.element = element

    @property
    def name(self):
        return self.element.find_element(By.CLASS_NAME, 'inventory_item_name').text

    @property
    def price(self):
        return self.element.find_element(By.CLASS_NAME, 'inventory_item_price').text

from Page.base_page import Page
from selenium.webdriver.common.by import By


class Cart(Page):
    EXPECTED_TEXT = (By.CSS_SELECTOR, ".a-row.sc-your-amazon-cart-is-empty")
    cart = (By.ID, 'nav-cart-count')
    PRODUCT_NAME_IN_CART = (By.CSS_SELECTOR, '.a-truncate-cut')
    actual_name_in_cart = ''
    PRODUCT_NAME = ''

    def cart_check(self):
        self.verify_text("Your Amazon Cart is empty", *self.EXPECTED_TEXT)
        print("Cart is empty!")

    def cart_page_open(self):
        self.open_page(end_url='gp/cart/view.html?ref_=nav_cart')

    def verify_item_count_in_cart(self, expected_count):
        actual_text = self.find_element(*self.cart).text
        assert expected_count == actual_text, f'Expected {expected_count} but got {actual_text}'

    def verify_product_name(self):
        self.actual_name_in_cart = self.find_element(*self.PRODUCT_NAME_IN_CART).text
        assert self.PRODUCT_NAME[:30] in self.actual_name_in_cart, f"Expected: {self.PRODUCT_NAME}," \
                                                                         f"but got: {self.actual_name_in_cart}"





from selenium.webdriver.common.by import By
from Page.base_page import Page


class Header(Page):
    search_field = (By.ID, "twotabsearchtextbox")
    search_btn = (By.ID, "nav-search-submit-button")
    returns_orders_btn = (By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']")
    cart_btn = (By.ID, "nav-cart-count-container")

    def search_product(self, keyword):
        self.input_text(keyword, *self.search_field)

    def click_search(self):
        self.click(*self.search_btn)

    def click_returns_orders_btn(self):
        self.find_element(*self.returns_orders_btn).click()

    def click_cart_btn(self):
        self.driver.find_element(*self.cart_btn).click()
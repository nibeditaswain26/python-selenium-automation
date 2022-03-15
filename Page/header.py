from selenium.webdriver.common.by import By
from Page.base_page import Page


class Header(Page):
    search_field = (By.ID, "twotabsearchtextbox")
    search_btn = (By.ID, "nav-search-submit-button")

    def search_product(self, keyword):
        self.input_text(keyword, *self.search_field)

    def click_search(self):
        self.click(*self.search_btn)

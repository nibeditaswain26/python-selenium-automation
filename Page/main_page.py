
from Page.base_page import Page


class MainPage(Page):
    def open_main(self):
        self.open_page()

    def open_amazon_product_page(self, product_id):
        self.open_page(f'dp/{product_id}/')

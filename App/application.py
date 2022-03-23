from Page.header import Header
from Page.main_page import MainPage
from Page.search_result_page import SearchResultPage
from Page.best_seller_page import BestSellerPage
from Page.sign_in_page import SignIn
from Page.cart_page import Cart
from Page.search_product_page import SearchProduct


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.search_result_page = SearchResultPage(self.driver)
        self.best_seller_page = BestSellerPage(self.driver)
        self.sign_in_page = SignIn(self.driver)
        self.cart_page = Cart(self.driver)
        self.search_product_page = SearchProduct(self.driver)


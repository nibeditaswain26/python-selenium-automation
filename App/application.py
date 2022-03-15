from Page.header import Header
from Page.main_page import MainPage
from Page.search_result_page import SearchResultPage
from Page.best_seller_page import BestSellerPage


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.search_result_page = SearchResultPage(self.driver)
        self.best_seller_page = BestSellerPage(self.driver)


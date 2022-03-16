from selenium.webdriver.common.by import By
from Page.base_page import Page


class BestSellerPage(Page):
    best_seller_links = (By.CSS_SELECTOR, '._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq li')
    best_seller_five_links = (By.CSS_SELECTOR, '._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq li')
    LINKS_HEADER_TEXT = (By.ID, 'zg_banner_text')

    def open_best_seller_page(self):
        self.open_page(end_url='gp/bestsellers/?ref_=nav_cs_bestsellers')

    def click_thru_links(self):
        b_s_links = self.driver.find_elements(*self.best_seller_five_links)  # [l_1, l_2, l_3, l_4, l_5]
        for li in range(0, len(b_s_links)):
            links = self.driver.find_elements(*self.best_seller_five_links)[li]
            links_text = links.text  # first store the text.
            links.click()  # then click on the links
            self.verify_partial_text(links_text, *self.LINKS_HEADER_TEXT)

    def verify_best_seller_links(self, expected_amount):
        best_seller_amount = len(self.find_elements(*self.best_seller_links))
        assert best_seller_amount == int(expected_amount), f"expected 5 links but got {best_seller_amount}"


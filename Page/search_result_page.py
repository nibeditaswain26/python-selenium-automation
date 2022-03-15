from selenium.webdriver.common.by import By

from Page.base_page import Page


class SearchResultPage(Page):
    RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")

    def verify_result(self, expected_result):
        self.verify_text(expected_result, *self.RESULT)
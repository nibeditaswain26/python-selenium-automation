from selenium.webdriver.common.by import By
from Page.base_page import Page


class SignIn(Page):
    def verify_sign_in_page(self):
        self.verify_url_contains_query('https://www.amazon.com/ap/signin')
        # assert "Amazon Sign-In" in self.driver.title
        # print("Email verify page open.")

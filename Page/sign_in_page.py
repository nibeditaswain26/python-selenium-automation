from selenium.webdriver.common.by import By
from Page.base_page import Page
from selenium.webdriver.support import expected_conditions as EC


class SignIn(Page):
    def verify_sign_in_page(self):
        self.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'), message='sign_in page not opened')
        # assert "Amazon Sign-In" in self.driver.title
        # print("Email verify page open.")

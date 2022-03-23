from selenium.webdriver.common.by import By
from Page.base_page import Page


class SearchResultPage(Page):
    RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    search_field = (By.ID, 'twotabsearchtextbox')
    search_button = (By.ID, 'nav-search-submit-button')
    product_price = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
    add_cart_button = (By.ID, 'add-to-cart-button')
    product_name = (By.ID, 'productTitle')
    PRODUCT_NAME = ""
    drop_down_department = (By.CSS_SELECTOR, '#nav-subnav[data-category="{department_category}"]')

    def _get_department_locator(self, department: str):
        return [self.drop_down_department[0], self.drop_down_department[1].replace("{department_category}", department)]

    def verify_result(self, expected_result):
        self.verify_text(expected_result, *self.RESULT)

    def click_first_product(self):
        self.find_element(*self.product_price).click()

    def get_product_name(self):
        self.PRODUCT_NAME = self.find_element(*self.product_name).text
        print(f"Product name is: {self.PRODUCT_NAME}")

    def click_add_cart_btn(self):
        self.find_element(*self.add_cart_button).click()

    def verify_correct_department(self, department):
        department_locator = self._get_department_locator(department)
        self.wait_for_element_appear(*department_locator)

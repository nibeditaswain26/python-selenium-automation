from Page.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class SearchProduct(Page):
    NEW_ARRIVALS_BTN = (By.CSS_SELECTOR, 'a[href="/New-Arrivals/b/?_encoding=UTF8&node=17020138011&ref_=sv_sl_6"]')
    MENU = (By.ID, 'nav-flyout-amazonfresh')

    def hover_new_arrival(self):
        new_arrivals = self.find_element(*self.NEW_ARRIVALS_BTN)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()

    def verify_new_deals(self):
        self.wait_for_element_appear(*self.MENU)


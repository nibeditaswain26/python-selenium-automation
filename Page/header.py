from selenium.webdriver.common.by import By
from Page.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class Header(Page):
    search_field = (By.ID, "twotabsearchtextbox")
    search_btn = (By.ID, "nav-search-submit-button")
    returns_orders_btn = (By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']")
    cart_btn = (By.ID, "nav-cart-count-container")
    flag_btn = (By.CSS_SELECTOR, ".icp-nav-flag.icp-nav-flag-us")
    spanish_option = (By.CSS_SELECTOR, '[href="#switch-lang=es_US"]')
    select_department = (By.ID, "searchDropdownBox")

    def search_product(self, keyword):
        self.input_text(keyword, *self.search_field)

    def click_search(self):
        self.click(*self.search_btn)

    def click_returns_orders_btn(self):
        self.find_element(*self.returns_orders_btn).click()

    def click_cart_btn(self):
        self.driver.find_element(*self.cart_btn).click()

    def hover_lang_options(self):
        flag = self.find_element(*self.flag_btn)
        actions = ActionChains(self.driver)
        actions.move_to_element(flag)
        actions.perform()

    def select_department_dropdown(self, alias):
        select_dep_box = self.find_element(*self.select_department)
        select = Select(select_dep_box)
        select.select_by_value(f'search-alias={alias}')

    def verify_spanish_lang(self):
        self.wait_for_element_appear(*self.spanish_option)


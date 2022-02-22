from selenium.webdriver.common.by import By
from behave import given, when, then

best_seller_links = (By.CSS_SELECTOR, '._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq li')


@given('Open Amazon best seller page')
def open_best_seller(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify user can see {expected_amount} links in best seller page')
def verify_best_seller_links(context, expected_amount):
    best_seller_amount = len(context.driver.find_elements(*best_seller_links))
    assert best_seller_amount == int(expected_amount), f"expected 5 links but got {best_seller_amount}"


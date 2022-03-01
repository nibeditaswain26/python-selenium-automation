from selenium.webdriver.common.by import By
from behave import given, when, then

cart = (By.ID, 'nav-cart-count')
PRODUCT_NAME_in_cart = (By.CSS_SELECTOR, '.a-truncate-cut')

@when('Open cart page')
def open_cart_page(context):
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')


@then('verify cart has {expected_count} item(s)')
def verify_cart_counts(context, expected_count):
    actual_text = context.driver.find_element(*cart).text
    assert expected_count == actual_text, f'Expected {expected_count} but got {actual_text}'


@then('verify cart has correct product')
def verify_product_name(context):
    context.actual_name_in_cart = context.driver.find_element(*PRODUCT_NAME_in_cart).text
    assert context.PRODUCT_NAME[:30] in context.actual_name_in_cart, f"Expected: {context.PRODUCT_NAME},"\
                                                                     f"but got: {context.actual_name_in_cart}"

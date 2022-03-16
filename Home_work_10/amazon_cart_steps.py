from selenium.webdriver.common.by import By
from behave import given, when, then

EXPECTED_TEXT = (By.CSS_SELECTOR, ".a-row.sc-your-amazon-cart-is-empty")


@given('Opens Amazon')
def open_amazon(context):
    context.app.main_page.open_main()


@when('clicks on the cart icon')
def cart_icon(context):
    context.app.header.click_cart_btn()


@then('verifies that Your Amazon Cart is empty')
def cart_empty(context):
    context.app.cart_page.cart_check()

from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Open cart page')
def open_cart_page(context):
    context.app.cart_page.cart_page_open()


@then('verify cart has {expected_count} item(s)')
def verify_cart_counts(context, expected_count):
    context.app.cart_page.verify_item_count_in_cart(expected_count)


@then('verify cart has correct product')
def verify_product_name(context):
    context.app.cart_page.verify_product_name()
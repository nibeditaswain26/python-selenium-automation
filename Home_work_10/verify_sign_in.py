from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on Return&Order')
def click_order(context):
    context.app.header.click_returns_orders_btn()


@then('Verify sign in page opened')
def verify_sign_in(context):
    context.app.sign_in_page.verify_sign_in_page()
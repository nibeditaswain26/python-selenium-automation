from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Opens Amazon')
def open_amazon(context):
    context.driver.get('https://Amazon.com')


@when('clicks on the cart icon')
def cart_icon(context):
    context.driver.find_element(By.ID, "nav-cart-count-container").click()


@then('verifies that Your Amazon Cart is empty')
def cart_empty(context):
    expected_text = context.driver.find_element(By.CSS_SELECTOR, ".a-row.sc-your-amazon-cart-is-empty").text
    actual_text = "Your Amazon Cart is empty"
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
    print("Cart is empty!")

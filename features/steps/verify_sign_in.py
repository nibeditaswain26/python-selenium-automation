from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on Return&Order')
def click_order(context):
    context.driver.find_element(By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()


@then('Verify sign in page opened')
def verify_sign_in(context):
    assert "Amazon Sign-In" in context.driver.title
    print("Email verify page open.")
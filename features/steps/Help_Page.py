from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@given('Open Amazon Help Page')
def amazon_help_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')
    # print("com_help") for debugging


@when('Use search help library field and search for Cancel order and Hitting keyboard ENTER btn with send_keys command')
def cancel_order(context):
    context.driver.find_element(By.ID, 'helpsearch').send_keys('Cancel Order', Keys.ENTER)
    # print("com_cancel") For debugging


@then("Verify that 'Cancel items or orders' text is present")
def verify_page(context,):
    actual_text = context.driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
    exepected_text = "Cancel Items or Orders"
    assert exepected_text == actual_text, f'Expected {exepected_text}, but got {actual_text}'
    # print("com_verify") # for debugging
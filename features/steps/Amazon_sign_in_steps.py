from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then


sign_in_popup = (By.CSS_SELECTOR, '#nav-signin-tooltip')


@when('click on sign in button from sign in popup')
def click_sign_in_popup(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(sign_in_popup), message='Sign in button not clickable'
    ).click()


@then('verify sign in page opened.')
def verify_sign_in_page_opened(context):
    context.driver.wait.until(
        EC.url_contains('https://www.amazon.com/ap/signin'), message='sign in page did not open'
    ) # check with the url

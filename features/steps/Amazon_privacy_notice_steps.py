from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

HEADER_OF_PAGE = (By.XPATH, '//h1[text()="Amazon.com Privacy Notice"]')


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_notice_page(context):
    context.driver.wait.until(EC.text_to_be_present_in_element(HEADER_OF_PAGE, "Amazon.com Privacy Notice"))


@then('User can close new window')
def close_new_wind(context):
    context.driver.close()
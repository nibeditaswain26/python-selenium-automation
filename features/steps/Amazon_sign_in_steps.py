from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then
from time import sleep


sign_in_popup = (By.CSS_SELECTOR, '#nav-signin-tooltip')


@when('click on sign in button from sign in popup')
def click_sign_in_popup(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(sign_in_popup), message='Sign in button not clickable'
    ).click()


@when('wait for {sec} sec')
def wait(context, sec):
    sleep(int(sec))


@then('verify sign in page opened.')
def verify_sign_in_page_opened(context):
    context.driver.wait.until(
        EC.url_contains('https://www.amazon.com/ap/signin'), message='sign in page did not open'
    ) # check with the url


@then('verify that sign in popup shown')
def verify_sign_in_popup(context):
    context.driver.wait.until(EC.visibility_of_element_located(sign_in_popup), message='sign in pop up not visible.')


@then('verify that sign in btn is clickable')
def sign_in_btn_clickable(context):
    context.driver.wait.until(EC.element_to_be_clickable(sign_in_popup), message='sign in btn not clickable.')


@then('verify sign in popup disappears')
def sign_in_disappears(context):
    context.driver.wait.until(EC.invisibility_of_element_located(sign_in_popup),message='sign in btn still visible')
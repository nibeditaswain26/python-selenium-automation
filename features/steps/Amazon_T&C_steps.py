from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

PRIVACY_NOTICE = (By.CSS_SELECTOR, '[href="https://www.amazon.com/privacy"]')


@given('Open Amazon T&C page')
def open_t_and_c_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html'
                       '/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088 ')


@when('Store original windows')
def store_ori_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)


@when('Click on Amazon Privacy Notice link')
def click_privacy_notice(context):
    context.driver.find_element(*PRIVACY_NOTICE).click()


@when('Switch to the newly opened window')
def switch_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    current_window = context.driver.window_handles # [win_1(current_win), win_2(new_opened_window)]
    context.driver.switch_to.window(current_window[1])


@then('Switch back to original')
def switch_back_original(context):
    context.driver.switch_to.window(context.original_window)

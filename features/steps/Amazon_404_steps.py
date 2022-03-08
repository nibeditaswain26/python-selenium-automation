from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

DOG_IMG = (By.CSS_SELECTOR, '#d[alt="Dogs of Amazon"]')


@given('Open Amazon product {Product_id} page')
def open_amazon_product(context, Product_id):
    context.driver.get(f'https://www.amazon.com/dp/{Product_id}/')


@given('Store original window')
def store_ori_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)


@when('Click on the dog image')
def click_dog_img(context):
    context.driver.find_element(*DOG_IMG).click()


@when('Switch to a new window')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    current_window = context.driver.window_handles
    print('current: ', current_window)
    context.driver.switch_to.window(current_window[1])


@then('Return to original window')
def return_ori_window(context):
    context.driver.switch_to.window(context.original_window)





from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

@then('Verify blog is opened')
def verify_blog(context):
    context.driver.wait.until(EC.url_contains('https://www.aboutamazon.com/'))


@then('Close blog window')
def close_blog_win(context):
    context.driver.close()
    current_window = context.driver.window_handles
    print('current: ', current_window)

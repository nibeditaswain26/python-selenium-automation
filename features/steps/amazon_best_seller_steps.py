from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon best seller page')
def open_best_seller(context):
    context.app.best_seller_page.open_best_seller_page()


@then('Verify user can see {expected_amount} links in best seller page')
def verify_best_seller_links(context, expected_amount):
    context.app.best_seller_page.verify_best_seller_links(expected_amount)


@then('Verify that correct page opens when user go through all the best seller links')
def verify_page(context):
    context.app.best_seller_page.click_thru_links()

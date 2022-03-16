from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Clik on the First product')
def click_on_the_first_product(context):
    context.app.search_result_page.click_first_product()


@when('Store the product name')
def get_product_name(context):
    context.app.search_result_page.get_product_name()


@when('click on add to cart button')
def click_add_to_cart(context):
    context.app.search_result_page.click_add_cart_btn()

    
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


@when('Hover over the language options')
def hover_lang_options(context):
    context.app.header.hover_lang_options()


@when('select department by alias {alias}')
def select_department(context, alias: str):
    context.app.header.select_department_dropdown(alias)


@then('Verify spanish option is present')
def verify_spanish_lang(context):
    context.app.header.verify_spanish_lang()


@then('Verify {department} department is selected')
def verify_correct_department(context, department):
    context.app.search_result_page.verify_correct_department(department)
    
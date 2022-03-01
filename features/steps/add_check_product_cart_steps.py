from selenium.webdriver.common.by import By
from behave import given, when, then

search_field = (By.ID, 'twotabsearchtextbox')
search_button = (By.ID, 'nav-search-submit-button')
product_price = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
add_cart_button = (By.ID, 'add-to-cart-button')
product_name = (By.ID, 'productTitle')


@when('Search for Urban Decay Naked Eyeshadow Palette')
def product_search(context):
    context.driver.find_element(*search_field).send_keys('mac eyeshadow palette')
    context.driver.find_element(*search_button).click()


@when('Clik on the First product')
def click_on_the_first_product(context):
    context.driver.find_element(*product_price).click()


@when('Store the product name')
def get_product_name(context):
    context.PRODUCT_NAME = context.driver.find_element(*product_name).text
    print(f"Product name is: {context.PRODUCT_NAME}")






@when('click on add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*add_cart_button).click()
    
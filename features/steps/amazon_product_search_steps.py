from selenium.webdriver.common.by import By
from behave import Given, When, Then


@When('Search for "coffee"')
def search_product(context):
    context.driver.find_element(By.ID, "twotabsearchtextbox").send_keys('coffee')
    context.driver.find_element(By.ID, "nav-search-submit-button").click()


from selenium.webdriver.common.by import By
from behave import Given, When, Then
search_field = (By.ID, "twotabsearchtextbox")
search_btn = (By.ID, "nav-search-submit-button")


@Given('Open Amazon')
def open_amazon(context):
    context.app.main_page.open_main()


@When('Search for {keyword}')
def search_product(context, keyword):
    context.app.header.search_product(keyword)
    context.app.header.click_search()




from selenium.webdriver.common.by import By
from behave import Given, When, Then

RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")


@Then('Verify search results are shown for {expected_result}')
def verify_result(context, expected_result):
     context.app.search_result_page.verify_result(expected_result)


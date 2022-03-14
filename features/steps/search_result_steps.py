from selenium.webdriver.common.by import By
from behave import Given, When, Then

@Then('Verify search results are shown')
def verify_result(context):
    expected_result = "coffee"
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text()
    assert expected_result == actual_result, f"expected text is {expected_result} did not match with {actual_result}."

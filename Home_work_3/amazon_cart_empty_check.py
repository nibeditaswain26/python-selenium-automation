from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path='/chromedriver.exe')
driver.maximize_window()

driver.get('https://Amazon.com')

driver.find_element(By.ID, "nav-cart-count-container").click()
expected_text = driver.find_element(By.CSS_SELECTOR, ".a-row.sc-your-amazon-cart-is-empty").text
actual_text = "Your Amazon Cart is empty"
assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
print("Cart is empty!")
driver.quit()

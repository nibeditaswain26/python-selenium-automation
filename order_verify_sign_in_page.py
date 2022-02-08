from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\Automation_study\python-selenium-automation\chromedriver.exe')
driver.maximize_window()

driver.get('https://Amazon.com')
driver.find_element(By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()
assert "Amazon Sign-In" in driver.title
print("Email verify page open.")
driver.quit()
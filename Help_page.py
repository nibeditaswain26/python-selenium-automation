from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path='C:\Automation_study\python-selenium-automation\chromedriver.exe')
driver.maximize_window()

# open the url
driver.get(' https://www.amazon.com/gp/help/customer/display.html ')
search_field = driver.find_element(By.ID, 'helpsearch')
search_item = search_field.send_keys('Cancel Order')
search_field.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source, f"The Text{search_item} is not found."
print("Text is present!")
driver.quit()
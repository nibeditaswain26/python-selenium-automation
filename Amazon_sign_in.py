from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\Automation_study\python-selenium-automation\chromedriver.exe')
driver.maximize_window()

# open the url
driver.get('https://Amazon.com')
sign_in = driver.find_element(By.ID, 'nav-link-accountList').click()

# locator for Amazon logo
driver.find_element(By.XPATH, "//*[@class='a-icon a-icon-logo']")

# locator for email field
driver.find_element(By.ID, 'ap_email').send_keys('nibeditaswain26@gmail.com')

# continue_field
driver.find_element(By.ID, 'continue').click()

# need help_link
driver.find_element(By.XPATH, "//a[@href ='javascript:void(0)']").click()

# forgot password_field
driver.find_element(By.ID, 'auth-fpp-link-bottom').click()

# Other issue with sign_in
driver.find_element(By.ID, 'ap-other-signin-issues-link').click()

# create your amazon account
driver.find_element(By.ID, 'createAccountSubmit').click()
driver.find_element(By.ID, 'ap_customer_name').send_keys('Nibedita')
driver.find_element(By.ID, 'ap_email').send_keys('nibeditaswain56@gmail.com')
driver.find_element(By.ID, 'ap_password').send_keys('Appleball@123')
driver.find_element(By.ID, 'ap_password_check').send_keys('Appleball@123')
driver.find_element(By.ID, 'continue').click()
# privacy_notice_link
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']").click()

# condition_of_use
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']").click()






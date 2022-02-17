from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path= "C:\Automation_study\python-selenium-automation\chromedriver.exe")
driver.maximize_window()

driver.get('https://Amazon.com')
driver.find_element(By.ID, 'nav-link-accountList').click()

driver.find_element(By.ID, 'createAccountSubmit').click()
# locator for logo
# driver.find_element(By.CSS_SELECTOR, '#.a-icon-logo')
# locator for create account heading
# driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')
# locator for "your name"
driver.find_element(By.ID, 'ap_customer_name').send_keys('Nibedita')
# locator for mobile_number or email
driver.find_element(By.ID, 'ap_email').send_keys('nibeditaswain26@gmail.com')
# locator for password
driver.find_element(By.ID, 'ap_password').send_keys('apple@123')
# locator for re-enter pwd
driver.find_element(By.ID, 'ap_password_check').send_keys('apple@123')
# locator for at_least_6_character
driver.find_element(By.XPATH, "//div[contains(text(),'Passwords must be at least 6 characters.')]")
# locator for continue
driver.find_element(By.ID, 'continue').click()
# locator for condition of use
driver.find_element(By.CSS_SELECTOR, 'a[href*="/gp/help/customer/display.html/ref='
                                     'ap_register_notification_condition_of_use"]').click()
# locator for privacy notice
driver.find_element(By.CSS_SELECTOR, 'a[href*="/gp/help/customer/display.html/ref='
                                     'ap_register_notification_privacy_notice?"]')
# locator for sign_in(already have account)
driver.find_element(By.XPATH, "//div[@class='a-row']//a[contains(@href, '/ap/signin?"
                              "openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fre')]")




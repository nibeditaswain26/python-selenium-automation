from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome('C:\Automation_study\python-selenium-automation\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(4)

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Watch')

# wait for 4 sec
# sleep(4) # function- allows you to stop the execution and wait for certain amount of time in sec


# click search
driver.find_element(By.NAME, 'btnK').click()

# verify
assert 'watch' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()

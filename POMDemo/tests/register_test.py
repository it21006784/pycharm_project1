import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://magento.softwaretestingboard.com/customer/account/create/")

# Fill out personal information
driver.find_element(By.ID, "firstname").send_keys("Mihi")
driver.find_element(By.ID, "lastname").send_keys("Jayaweera")

# Fill out sign-in information
driver.find_element(By.ID, "email_address").send_keys("mihi@gmail.com")
driver.find_element(By.ID, "password").send_keys("mihi@12345")
driver.find_element(By.ID, "password-confirmation").send_keys("mihi@12345")

# Locate the button
button = driver.find_element(By.XPATH, "//button[@class='action submit primary' and @title='Create an Account']")
button.click()

act_title = driver.title
exp_title = "Create New Customer Account"

if act_title == exp_title:
    print("Registration Test Passed")
else:
    print("Registration Test Failed")

time.sleep(2)
driver.close()

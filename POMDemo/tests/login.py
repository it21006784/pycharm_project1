import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://magento.softwaretestingboard.com/")

driver.find_element(By.LINK_TEXT, "Sign In").click()

driver.find_element(By.ID,"email").send_keys("mihi@gmail.com")
driver.find_element(By.ID,"pass").send_keys("mihi@12345")
driver.find_element(By.ID,"send2").click()

act_title = driver.title
exp_title = "Home Page"

if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

time.sleep(2)
driver.close()
import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://magento.softwaretestingboard.com/")

women_category = driver.find_element(By.XPATH, "//a[text()='Women']")

#hover action
action = ActionChains(driver)
action.move_to_element(women_category).perform()
time.sleep(2)

driver.find_element(By.XPATH, "//a[text()='Tops']").click()
time.sleep(2)

driver.find_element(By.ID, "ui-id-11").click()
time.sleep(3)
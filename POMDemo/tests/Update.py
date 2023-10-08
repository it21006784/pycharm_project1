import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://magento.softwaretestingboard.com/")

driver.find_element(By.LINK_TEXT, "Sign In").click()

driver.find_element(By.ID,"email").send_keys("mihi@gmail.com")
driver.find_element(By.ID,"pass").send_keys("mihi@12345")
driver.find_element(By.ID,"send2").click()

driver.find_element(By.CSS_SELECTOR,"a.action.showcart").click()
# driver.find_element(By.LINK_TEXT, "View and Edit Cart").click()
driver.get("https://magento.softwaretestingboard.com/checkout/cart/")

driver.find_element(By.CSS_SELECTOR,"a.action.action-edit").click()

# driver.find_element(By.ID, "option-label-size-143-item-168").click()

quantity_input = driver.find_element(By.ID, "qty")
quantity_input.clear()
quantity_input.send_keys("4")

driver.find_element(By.ID, "product-updatecart-button").click()

success_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Riona Full Zip Jacket was updated in your shopping cart.')]")))
exp_title = success_message.get_attribute("innerHTML")

act_title = driver.title.strip()

if act_title == exp_title:
    print("Update Test Passed")
else:
    print("Update Test Failed")

# Close the browser
driver.quit()
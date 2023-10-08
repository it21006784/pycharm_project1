import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://magento.softwaretestingboard.com/")

search_input = driver.find_element(By.ID, "search")
search_input.send_keys("girls wear")

search_input.send_keys(Keys.RETURN)

time.sleep(3)

act_title = driver.title
exp_title = "Search results for: 'girls wear'"

if act_title == exp_title:
    print("Search Test Passed")
else:
    print("Search Test Failed")

# Close the browser
driver.quit()
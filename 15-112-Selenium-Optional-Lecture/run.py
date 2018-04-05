from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

# Get a driver
options = Options()
options.add_argument('--disable-notifications')
driver = webdriver.Chrome(chrome_options=options)
driver.implicitly_wait(10)

# Load our page
driver.get("https://www.facebook.com")

userNameField = driver.find_element_by_id("email")
passwordField = driver.find_element_by_id("pass")
userNameField.send_keys("112stylegrader@gmail.com")
passwordField.send_keys("")
submit_button = driver.find_element_by_xpath("//*[@data-testid='royal_login_button']")
submit_button.click()

driver.get("https://www.facebook.com/pokes")

for element in driver.find_elements_by_xpath("//*[contains(text(), 'Poke Back')]"):
    element.click()

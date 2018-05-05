from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#get the driver
options = Options()
options.add_argument('--disable-notifications')
driver = webdriver.Chrome(chrome_options=options)

driver.get("https://www.facebook.com")

emailField = driver.find_element_by_id("email")
emailField.send_keys("112stylegrader@gmail.com")

passwordField = driver.find_element_by_id("pass")
passwordField.send_keys("reallystrongpassword")

loginButton = driver.find_element_by_id("u_0_2")
loginButton.click()

driver.get("https://www.facebook.com/pokes")

poke_buttons = driver.find_elements_by_xpath("//*[contains(text(), 'Poke Back')]")

for button in poke_buttons:
    button.click()







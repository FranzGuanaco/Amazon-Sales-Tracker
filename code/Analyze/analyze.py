import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Configure the Firefox driver to download files to the desired directory
firefox_options = Options()
download_dir = os.path.join(os.getcwd(), 'downloads')
os.makedirs(download_dir, exist_ok=True)

firefox_options.set_preference("browser.download.folderList", 2)
firefox_options.set_preference("browser.download.manager.showWhenStarting", False)
firefox_options.set_preference("browser.download.dir", download_dir)
firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,application/vnd.ms-excel")

# Create a Service object with the path to geckodriver
firefox_service = Service('/Users/pierrechevin/Downloads/geckodriver')

# Pass the Service object and options to the webdriver.Firefox()
driver = webdriver.Firefox(service=firefox_service, options=firefox_options)

# Load the web page
driver.get('https://members.helium10.com/black-box/products?accountId=1543470661')
sleep(5)  # Add a pause to allow the page to load

# Replace with your credentials
username = 'chevin.pierre.tomas@gmail.com'
password = 'Elsalvador60?'

# Replace with the appropriate CSS selectors
username_selector = '#loginform-email'
password_selector = '#loginform-password'
login_button_selector = '.btn.btn-secondary.btn-block'

# Locate the username and password fields and the login button
username_field = driver.find_element(By.CSS_SELECTOR, username_selector)
password_field = driver.find_element(By.CSS_SELECTOR, password_selector)
login_button = driver.find_element(By.CSS_SELECTOR, login_button_selector)

# Fill in the input fields with your credentials
username_field.send_keys(username)
password_field.send_keys(password)

# Click on the login button
login_button.click()

sleep(35)

# Replace with the appropriate CSS selector for the search input
search_input_selector = '[data-testid="search"]'
search_input = driver.find_element(By.CSS_SELECTOR, search_input_selector)

# Scroll to the search input element using JavaScript
driver.execute_script("arguments[0].scrollIntoView();", search_input)

sleep(15)

# tout marche
search_input.click()

sleep(15)

# Replace with the appropriate CSS selector for the download button
download_button_selector = '.sc-ezbkAF.sc-frCSdB.jMqZzF.cdqGrQ.sc-eoZuQF.jusArX.sc-eoZuQF.jusArX'
download_button = driver.find_element(By.CSS_SELECTOR, download_button_selector)

# Click on the download button
download_button.click()

sleep(13)

dropdown_button_selector = '.sc-ehCJOs.aRWDJ'
dropdown_button = driver.find_element(By.CSS_SELECTOR, dropdown_button_selector)
dropdown_button.click()

# Wait for the file to be downloaded
sleep(10)

# Close the browser
driver.quit()



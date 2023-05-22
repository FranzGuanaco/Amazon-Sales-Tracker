import os
import selenium
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

print(selenium.__version__)

# Configurez le pilote Firefox pour télécharger le fichier dans le répertoire souhaité
firefox_options = Options()
download_dir = os.path.join(os.getcwd(), 'downloads')
os.makedirs(download_dir, exist_ok=True)

firefox_options.set_preference("browser.download.folderList", 2)
firefox_options.set_preference("browser.download.manager.showWhenStarting", False)
firefox_options.set_preference("browser.download.dir", download_dir)
firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,application/vnd.ms-excel")

# Passez l'objet de service à la méthode webdriver.Firefox()
driver = webdriver.Firefox(executable_path='/Users/pierrechevin/Downloads/geckodriver', options=firefox_options)

# Chargez la page web
driver.get('https://members.helium10.com/black-box/products?accountId=1543470661')
sleep(5)  # Ajoutez une pause pour que la page ait le temps de se charger

# Remplacez par vos identifiants
username = 'chevin.pierre.tomas@gmail.com'
password = 'Elsalvador60?'

# Remplacez par les sélecteurs CSS appropriés
username_selector = '#loginform-email'
password_selector = '#loginform-password'
login_button_selector = '.btn.btn-secondary.btn-block'

# Localisez les champs de saisie des identifiants et le bouton de connexion
username_field = driver.find_element("css selector", "#loginform-email")
password_field = driver.find_element("css selector", password_selector)
login_button = driver.find_element("css selector", login_button_selector)

# Remplissez les champs de saisie avec vos identifiants
username_field.send_keys(username)
password_field.send_keys(password)

# Cliquez sur le bouton de connexion
login_button.click()

# Attendez que la page se charge complètement (ajustez le temps d'attente si nécessaire)
sleep(5)

# Localisez le bouton de téléchargement et cliquez dessus
# Assurez-vous que le sélecteur CSS est correct
download_button_selector = '.sc-llYSUQ.bhKSKZ'  # Ici, il manque un point entre les deux classes
download_button = driver.find_element_by_css_selector(download_button_selector)
download_button.click()

# Attendez que le fichier soit téléchargé
sleep(10)

# Fermez le navigateur
driver.quit()

# Maintenant, vous pouvez lire le fichier Excel avec pandas

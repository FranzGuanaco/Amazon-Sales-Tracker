import os
import selenium
import subprocess
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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
sleep(20)
# Cliquez sur le bouton de connexion
login_button.click()

sleep(5)

# Localisez le bouton de téléchargement et cliquez dessus
# Assurez-vous que le sélecteur CSS est correct
# Localisez le bouton de téléchargement
download_button_selector = '.sc-ikJyIC.kmfDQj'  # Sélecteur CSS du bouton de téléchargement
download_button = driver.find_element("css selector", download_button_selector)

# Faites défiler l'élément dans la vue
driver.execute_script("arguments[0].scrollIntoView(true);", download_button)

# Cliquez sur le bouton de téléchargement à l'aide de JavaScript
driver.execute_script("arguments[0].click();", download_button)

# Attendez que le fichier soit téléchargé
sleep(10)

# Localisez le bouton déroulant
dropdown_button_selector = '.sc-ikJyIC.sc-hrjYtz.jKrrPL.dXeRAJ.sc-gHERNO.dDsDpY'
dropdown_button = driver.find_element("css selector", dropdown_button_selector)

# Cliquez sur le bouton déroulant
dropdown_button.click()

sleep(1)

# Localisez le bouton de téléchargement du document
download_button_selector = '.sc-caiLqq.haRiMa'
download_button = driver.find_element("css selector", download_button_selector)

# Cliquez sur le bouton de téléchargement du document
download_button.click()

sleep(3)

download_dir = os.path.join(os.getcwd(), 'downloads')

# Liste tous les fichiers du répertoire de téléchargement
files = os.listdir(download_dir)

# Parcourez les fichiers et ouvrez le fichier souhaité
for file in files:
    if file.endswith('.csv'):  # Remplacez '.csv' par l'extension de votre fichier
        file_path = os.path.join(download_dir, file)
        # Ouvre le fichier avec l'application par défaut du système
        if sys.platform.startswith('darwin'):  # Pour macOS
            subprocess.call(['open', file_path])
        elif sys.platform.startswith('win32'):  # Pour Windows
            subprocess.call(['start', file_path], shell=True)
        elif sys.platform.startswith('linux'):  # Pour Linux
            subprocess.call(['xdg-open', file_path])
        break

sleep(12)

# Fermez le navigateur
driver.quit()


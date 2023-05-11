import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configurez le pilote Chrome pour télécharger le fichier dans le répertoire souhaité
chrome_options = Options()
download_dir = os.path.join(os.getcwd(), 'downloads')
os.makedirs(download_dir, exist_ok=True)

chrome_options.add_experimental_option(
    "prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True
    }
)

# Initialisez le pilote Chrome avec les options spécifiées
driver = webdriver.Chrome(executable_path='/Users/pierrechevin/Downloads/driverchrome/chromedriver', options=chrome_options)

# Chargez la page web
driver.get('https://members.helium10.com/black-box/products?accountId=1543470661')

# Remplacez par vos identifiants
username = 'chevin.pierre.tomas@gmail.com'
password = 'Elsalvador60?'

# Remplacez par les sélecteurs CSS appropriés
username_selector = '#loginform-email'
password_selector = '#loginform-password'
login_button_selector = '.btn btn-secondary btn-block'

# Localisez les champs de saisie des identifiants et le bouton de connexion
username_field = driver.find_element_by_css_selector(username_selector)
password_field = driver.find_element_by_css_selector(password_selector)
login_button = driver.find_element_by_css_selector(login_button_selector)

# Remplissez les champs de saisie avec vos identifiants
username_field.send_keys(username)
password_field.send_keys(password)

# Cliquez sur le bouton de connexion
login_button.click()

# Attendez que la page se charge complètement (ajustez le temps d'attente si nécessaire)
sleep(5)

# Localisez le bouton de téléchargement et cliquez dessus
download_button = driver.find_element_by_css_selector('.sc-llYSUQ bhKSKZ')
download_button.click()

# Attendez que le fichier soit téléchargé
sleep(10)

# Fermez le navigateur
driver.quit()

# Maintenant, vous pouvez lire le fichier Excel avec pandas

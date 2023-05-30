import matplotlib.pyplot as plt
import pandas as pd
from pymongo import MongoClient

df = pd.read_csv('Analyze/AMZ_Data_Clean.csv')

# Liste des catégories de prix
price_ranges = [0, 100, 200, 300, 400, 500, 1000]

# Nombre moyen de vendeurs actifs par catégorie de prix
avg_sellers_per_price = []
for i in range(len(price_ranges) - 1):
    price_df = df.loc[(df['Price'] >= price_ranges[i]) & (df['Price'] < price_ranges[i + 1]), ['Number of Active Sellers']]
    total_sellers = price_df['Number of Active Sellers'].sum()
    num_rows = price_df.shape[0]
    avg_sellers = round(total_sellers / num_rows, 1) if num_rows > 0 else 0
    avg_sellers_per_price.append(avg_sellers)

# Création du graphique
plt.bar(price_ranges[:-1], avg_sellers_per_price)

# Configuration des labels et des titres
plt.xlabel('Prix')
plt.ylabel('Nombre moyen de vendeurs actifs')
plt.title('Nombre moyen de vendeurs actifs par catégorie de prix')
plt.xticks(price_ranges[:-1], rotation=90)

# Affichage du graphique
plt.show()

# Connexion à la base de données MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélection de la base de données
db = client['mydatabase']

# Sélection de la collection dans laquelle vous souhaitez insérer les données
collection = db['SellerPerCat']

data = []
for price, seller in zip(price_ranges, avg_sellers_per_price):
    data.append({'Category': price, 'Average seller': seller})

collection.insert_many(data)
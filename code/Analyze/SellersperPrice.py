import matplotlib.pyplot as plt
import pandas as pd
from pymongo import MongoClient
import numpy as np

df = pd.read_csv('Analyze/AMZ_Data_Clean.csv')

print(df.columns)

# Catégories de prix
# Définition des intervalles de prix pour chaque catégorie
price_ranges = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400]

# Liste pour stocker les vendeurs moyens par catégorie de prix
total_sellers_per_price = []

# Boucle à travers les catégories de prix et filtrage des données correspondantes
for i in range(len(price_ranges)):
    if i == len(price_ranges)-1:
        price_df = df.loc[(df['Price'] >= price_ranges[i]), ['Price', 'Number of Active Sellers']]
    else:
        price_df = df.loc[(df['Price'] >= price_ranges[i]) & (df['Price'] < price_ranges[i+1]), ['Price', 'Number of Active Sellers']]
    total_sellers = price_df['Number of Active Sellers'].sum()
    total_sellers_per_price.append(total_sellers)

# Tracé du graphique à barres
plt.bar(price_ranges[:-1], total_sellers_per_price[:-1])

# Configuration des étiquettes et du titre
plt.xlabel('Catégories de prix')
plt.ylabel('Vendeurs moyens')
plt.title('Vendeurs par catégorie de prix')

# Affichage du graphique
plt.show()

client = MongoClient('mongodb://localhost:27017/')

# Sélection de la base de données
db = client['mydatabase']

# Sélection de la collection dans laquelle vous souhaitez insérer les données
collection = db['SellerPerPrice']

data = []
for i in range(len(price_ranges)-1):
    data.append({'Price Range': f'{price_ranges[i]}-{price_ranges[i+1]}', 'Sellers': total_sellers_per_price[i].item()})

collection.insert_many(data)




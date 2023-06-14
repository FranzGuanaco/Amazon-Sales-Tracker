import matplotlib.pyplot as plt
import pandas as pd
from pymongo import MongoClient

df = pd.read_csv('Analyze/AMZ_Data_Clean.csv')

df['Reviews Rating'] = df['Reviews Rating'].dropna()
unique_values = df['Reviews Rating'].unique()
sorted_unique_values = sorted([x for x in unique_values if pd.notna(x)])

average_prices = {}

for note in sorted_unique_values:
    prices_for_note = df.loc[df['Reviews Rating'] == note, 'Price']
    average_price = prices_for_note.mean()
    average_prices[note] = average_price

# Afficher les moyennes des prix pour chaque note
for note, avg_price in average_prices.items():
    print(f"Note {note}: Moyenne des prix = {avg_price}")

# Tracé du graphique en ligne
plt.plot(sorted_unique_values, list(average_prices.values()), marker='o')

# Configuration des étiquettes et du titre
plt.xlabel('Notes')
plt.ylabel('Prix moyen')
plt.title('Prix moyen par note')

# Affichage du graphique
plt.show()
print(sorted_unique_values[1])

# Connexion à la base de données MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélection de la base de données
db = client['mydatabase']

# Sélection de la collection dans laquelle vous souhaitez insérer les données
collection = db['ReviewPerPrice']

data = []
for review, sellercat in zip(sorted_unique_values, list(average_prices.values())):
    data.append({'Review': review, 'Average Price': sellercat})

collection.insert_many(data)

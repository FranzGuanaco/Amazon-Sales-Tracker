import matplotlib.pyplot as plt
import pandas as pd
from pymongo import MongoClient

df = pd.read_csv('Analyze/AMZ_Data_Clean.csv')

# Liste des catégories
categories = df['Category'].unique()


total_revenue_per_category = []
for revenue in categories:
    revenue_df = df.loc[df['Category'] == revenue, ['Monthly Revenue']]
    total_revenue = revenue_df['Monthly Revenue'].sum()
    total_revenue_per_category.append(total_revenue)

sorted_categories, sorted_avg_sales = zip(*sorted(zip(categories, total_revenue_per_category), key=lambda x: x[1], reverse=True))

# Création du graphique
plt.bar(sorted_categories, sorted_avg_sales)

# Configuration des labels et des titres
plt.xlabel('Catégories')
plt.ylabel('Total de vente mensuelle (en dollars)')
plt.title('Total de vente pour chaque catégorie')
plt.xticks(rotation=90)

# Affichage du graphique
plt.show()

# Connexion à la base de données MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélection de la base de données
db = client['mydatabase']

# Sélection de la collection dans laquelle vous souhaitez insérer les données
collection = db['MonthlyRevenueperCat']

data = []
for category, monthly_revenue in zip(categories, total_revenue_per_category):
    data.append({'Category': category, 'Average Images': monthly_revenue})

collection.insert_many(data)

import matplotlib.pyplot as plt
import pandas as pd
from pymongo import MongoClient

df = pd.read_csv('Analyze/AMZ_Data_Clean.csv')

# Liste des catégories
categories = df['Category'].unique()

# Total de vente par catégories
total_seller_per_category = []
for seller in categories:
    sellers_df = df.loc[df['Category'] == seller, ['Reviews Rating']]
    total_sellers = sellers_df['Reviews Rating'].sort_values(ascending=True)

    if len(total_sellers) % 2 == 0:
        result = len(total_sellers)//2
        median = total_sellers.iloc[result]
    else:
        result = len(total_sellers)//2
        median_1 = result - 1
        median = (total_sellers.iloc[result] + total_sellers.iloc[median_1]) / 2

    total_seller_per_category.append(median)
        

sorted_categories, sorted_avg_sellers = zip(*sorted(zip(categories, total_seller_per_category), key=lambda x: x[1], reverse=True))

# Création du graphique
plt.bar(sorted_categories, sorted_avg_sellers)

# Configuration des labels et des titres
plt.xlabel('Catégories')
plt.ylabel('Moyenne des notes')
plt.title('Moyenne des notes par catégories')
plt.xticks(rotation=90)

# Affichage du graphique
plt.show()
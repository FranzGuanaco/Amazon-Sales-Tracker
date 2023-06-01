import matplotlib.pyplot as plt
import pandas as pd
from pymongo import MongoClient

df = pd.read_csv('Analyze/AMZ_Data_Clean.csv')

# Liste des catégories
categories = df['Category'].unique()

#etendre les valeurs
#diviser pas deux ou faire la moyenne du milieu
total_revenue_per_category = []
for revenue in categories:
    revenue_df = df.loc[df['Category'] == revenue, ['Monthly Revenue']]
    total_revenue_sorted = revenue_df['Monthly Revenue'].sort_values(ascending=True)
    
    if len(total_revenue_sorted) % 2 != 0:
        median_index = len(total_revenue_sorted) // 2
        median = total_revenue_sorted.iloc[median_index]
    else:
        median_index_1 = len(total_revenue_sorted) // 2
        median_index_2 = median_index_1 - 1
        median = (total_revenue_sorted.iloc[median_index_1] + total_revenue_sorted.iloc[median_index_2]) / 2
    
    total_revenue_per_category.append(median)

sorted_categories, sorted_avg_sales = zip(*sorted(zip(categories, total_revenue_per_category), key=lambda x: x[1], reverse=True))

# Création du graphique
plt.bar(sorted_categories, sorted_avg_sales)

# Configuration des labels et des titres
plt.xlabel('Catégories')
plt.ylabel('Mediane de vente mensuelle (en dollars)')
plt.title('Mediane de vente pour chaque catégorie')
plt.xticks(rotation=90)

# Affichage du graphique
plt.show()



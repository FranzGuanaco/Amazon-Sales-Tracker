import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Analyze/AMZ_Data_Clean.csv')

# Catégories de prix
# Définition des intervalles de prix pour chaque catégorie
price_ranges = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400]

# Liste pour stocker les vendeurs moyens par catégorie de prix
total_sellers_per_price = []

# Boucle à travers les catégories de prix et filtrage des données correspondantes
for i in range(len(price_ranges)):
    if i == len(price_ranges)-1:
        price_df = df.loc[(df['Price'] >= price_ranges[i]), ['Number of Active Sellers']]
    else:
        price_df = df.loc[(df['Price'] >= price_ranges[i]) & (df['Price'] < price_ranges[i+1]), ['Number of Active Sellers']]
    total_sellers = price_df['Number of Active Sellers'].sum()
    num_rows = price_df.shape[0]
    avg_sellers = round(total_sellers / num_rows, 1)
    total_sellers_per_price.append(total_sellers)

print (price_df)
# Tracé du graphique à barres
plt.bar(price_ranges[:-1], total_sellers_per_price[:-1])

# Configuration des étiquettes et du titre
plt.xlabel('Catégories de prix')
plt.ylabel('Vendeurs moyens')
plt.title('Vendeurs  par catégorie de prix')

# Affichage du graphique
plt.show()

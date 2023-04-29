import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Analyze/AMZ_Data_Clean.csv')

# Catégories de prix

# Définition des intervalles de prix pour chaque catégorie
price_ranges = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400]

# Liste pour stocker les ventes moyennes par catégorie de prix
total_sales_per_price = []

# Boucle à travers les catégories de prix et filtrage des données correspondantes
for i in range(len(price_ranges)):
    if i == len(price_ranges)-1:
        price_df = df.loc[(df['Price'] >= price_ranges[i]), ['Monthly Sales']]
    else:
        price_df = df.loc[(df['Price'] >= price_ranges[i]) & (df['Price'] < price_ranges[i+1]), ['Monthly Sales']]
    total_sales = price_df['Monthly Sales'].sum()
    num_rows = price_df.shape[0]
    avg_sales = round(total_sales / num_rows, 1)
    total_sales_per_price.append(avg_sales)


# Tracé du graphique à barres
plt.bar(price_ranges, total_sales_per_price)

# Configuration des étiquettes et du titre
plt.xlabel('Catégories de prix')
plt.ylabel('Ventes moyennes')
plt.title('Ventes moyennes par catégorie de prix')

# Affichage du graphique
plt.show()
print(price_ranges[0+1])


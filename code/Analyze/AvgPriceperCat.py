import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Analyze/AMZ_Data_Clean.csv')

# Liste des catégories
categories = ['Electronics', 'Home & Kitchen', 'Video Games', 'Books', 'Software', 'Computers & Accessories', 
              'Camera & Photo', 'Sports & Outdoors', 'Musical Instruments', 'Toys & Games', 'Patio, Lawn & Garden', 
              'Pet Supplies', 'Office Products', 'Arts, Crafts & Sewing', 'Baby Products', 'Grocery & Gourmet Food', 
              'Cell Phones & Accessories', 'Health & Household', 'Handmade Products', 'Beauty & Personal Care', 'Appliances', 
              'Clothing, Shoes & Jewelry', 'Industrial & Scientific', 'Tools & Home Improvement', 'Kitchen & Dining', 
              'Movies & TV', 'CDs & Vinyl']

# Total de vente par catégories
total_prices_per_category = []
for price in categories:
    price_df = df.loc[df['Category'] == price, ['Price']]
    total_prices = price_df['Price'].sum()
    num_rows = price_df.shape[0]
    avg_prices = round(total_prices / num_rows, 1)
    total_prices_per_category.append(avg_prices)

sorted_prices, sorted_avg_prices = zip(*sorted(zip(categories, total_prices_per_category), key=lambda x: x[1], reverse=True))


# Création du graphique
plt.bar(sorted_prices, sorted_avg_prices)

# Configuration des labels et des titres
plt.xlabel('Catégories')
plt.ylabel('Prix moyens')
plt.title('Moyenne de prix pour chaque catégorie')
plt.xticks(rotation=90)

# Affichage du graphique
plt.show()
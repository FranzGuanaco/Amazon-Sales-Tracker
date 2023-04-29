import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Analyze/AMZ_Data_Clean.csv')

# Liste des catégories
categories = ['Electronics', 'Home & Kitchen', 'Video Games', 'Books', 'Software', 'Computers & Accessories', 'Camera & Photo', 'Sports & Outdoors', 'Musical Instruments', 'Toys & Games', 'Patio, Lawn & Garden', 'Pet Supplies', 'Office Products', 'Arts, Crafts & Sewing', 'Baby Products', 'Grocery & Gourmet Food', 'Cell Phones & Accessories', 'Health & Household', 'Handmade Products', 'Beauty & Personal Care', 'Appliances', 'Clothing, Shoes & Jewelry', 'Industrial & Scientific', 'Tools & Home Improvement', 'Kitchen & Dining', 'Movies & TV', 'CDs & Vinyl']

# Total de vente par catégories
total_sales_per_category = []
for sales in categories:
    sales_df = df.loc[df['Category'] == sales, ['Monthly Sales']]
    total_sales = sales_df['Monthly Sales'].sum()
    num_rows = sales_df.shape[0]
    avg_sales = round(total_sales / num_rows, 1)
    total_sales_per_category.append(avg_sales)

sorted_categories, sorted_avg_sales = zip(*sorted(zip(categories, total_sales_per_category), key=lambda x: x[1], reverse=True))

# Création du graphique
plt.bar(sorted_categories, sorted_avg_sales)

# Configuration des labels et des titres
plt.xlabel('Catégories')
plt.ylabel('Total des ventes')
plt.title('Moyenne de vente pour chaque catégorie')
plt.xticks(rotation=90)

# Affichage du graphique
plt.show()
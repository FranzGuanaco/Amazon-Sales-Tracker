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


total_revenue_per_category = []
for revenue in categories:
    revenue_df = df.loc[df['Category'] == revenue, ['Monthly Revenue']]
    total_revenue = revenue_df['Monthly Revenue'].sum()
    num_rows = revenue_df.shape[0]
    avg_sales = round(total_revenue / num_rows, 1)
    total_revenue_per_category.append(avg_sales)

sorted_categories, sorted_avg_sales = zip(*sorted(zip(categories, total_revenue_per_category), key=lambda x: x[1], reverse=True))

# Création du graphique
plt.bar(sorted_categories, sorted_avg_sales)

# Configuration des labels et des titres
plt.xlabel('Catégories')
plt.ylabel('Moyenne de vente mensuelle (en dollars)')
plt.title('Moyenne de vente pour chaque catégorie')
plt.xticks(rotation=90)

# Affichage du graphique
plt.show()

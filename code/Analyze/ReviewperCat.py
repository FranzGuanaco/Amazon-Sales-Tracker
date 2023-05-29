import matplotlib.pyplot as plt
import pandas as pd
from pymongo import MongoClient

df = pd.read_csv('Analyze/AMZ_Data_Clean.csv')

# Liste des catégories
categories = ['Electronics', 'Home & Kitchen', 'Video Games', 'Books', 'Software', 'Computers & Accessories', 'Camera & Photo', 'Sports & Outdoors', 'Musical Instruments', 'Toys & Games', 'Patio, Lawn & Garden', 'Pet Supplies', 'Office Products', 'Arts, Crafts & Sewing', 'Baby Products', 'Grocery & Gourmet Food', 'Cell Phones & Accessories', 'Health & Household', 'Handmade Products', 'Beauty & Personal Care', 'Appliances', 'Clothing, Shoes & Jewelry', 'Industrial & Scientific', 'Tools & Home Improvement', 'Kitchen & Dining', 'Movies & TV', 'CDs & Vinyl']

# Total de vente par catégories
total_seller_per_category = []
for seller in categories:
    sellers_df = df.loc[df['Category'] == seller, ['Reviews Rating']]
    total_sellers = sellers_df['Reviews Rating'].sum()
    num_rows = sellers_df.shape[0]
    avg_sellers = round(total_sellers / num_rows, 1)
    total_seller_per_category.append(avg_sellers)

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

# Connexion à la base de données MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélection de la base de données
db = client['mydatabase']

# Sélection de la collection dans laquelle vous souhaitez insérer les données
collection = db['ReviewPerCat']

data = []
for cat, seller in zip(sorted_categories, sorted_avg_sellers):
    data.append({'Category': cat, 'Seller': seller})

collection.insert_many(data)


# Vérifier les collections dans la base de données
print(db.list_collection_names())
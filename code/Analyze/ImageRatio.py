import matplotlib.pyplot as plt
import pandas as pd
from pymongo import MongoClient

df = pd.read_csv('Analyze/AMZ_Data_Clean.csv')

# Liste des catégories
categories = ['Electronics', 'Home & Kitchen', 'Video Games', 'Books', 'Software', 'Computers & Accessories', 'Camera & Photo', 'Sports & Outdoors', 'Musical Instruments', 'Toys & Games', 'Patio, Lawn & Garden', 'Pet Supplies', 'Office Products', 'Arts, Crafts & Sewing', 'Baby Products', 'Grocery & Gourmet Food', 'Cell Phones & Accessories', 'Health & Household', 'Handmade Products', 'Beauty & Personal Care', 'Appliances', 'Clothing, Shoes & Jewelry', 'Industrial & Scientific', 'Tools & Home Improvement', 'Kitchen & Dining', 'Movies & TV', 'CDs & Vinyl']

# Calcule la moyenne du nombre d'images par produit pour chaque catégorie
avg_images_per_category = []
for cat in categories:
    cat_df = df.loc[df['Category'] == cat, ['Number of Images']]
    total_images = cat_df['Number of Images'].sum()
    num_rows = cat_df.shape[0]
    avg_images = round(total_images / num_rows, 1)
    avg_images_per_category.append(avg_images)

# Trier les catégories et les valeurs moyennes ensemble par ordre décroissant
sorted_categories, sorted_avg_images = zip(*sorted(zip(categories, avg_images_per_category), key=lambda x: x[1], reverse=True))

# Création du graphique
plt.bar(sorted_categories, sorted_avg_images)

# Configuration des labels et des titres
plt.xlabel('Catégories')
plt.ylabel('Moyenne de nombre d\'images par produit')
plt.title('Moyenne de nombre d\'images par produit pour chaque catégorie')
plt.xticks(rotation=90)

# Affichage du graphique
plt.show()

# Connexion à la base de données MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélection de la base de données
db = client['mydatabase']

# Convertir les données du DataFrame en une liste de dictionnaires (documents)
data = df.to_dict(orient='records')

# Sélection de la collection dans laquelle vous souhaitez insérer les données
collection = db['mycollection']

# Insérer les données dans la collection
collection.insert_many(data)

# Vérifier les collections dans la base de données
print(db.list_collection_names())








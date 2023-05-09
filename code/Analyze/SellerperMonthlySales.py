import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Analyze/AMZ_Data_Clean.csv')

# Création des catégories de ventes mensuelles
bins = [0, 10, 20, 30, 310]
labels = ['1-10', '11-20', '21-30', '31-310']
df['Monthly Sales Category'] = pd.cut(df['Monthly Sales'], bins=bins, labels=labels)

# Calcul du nombre de vendeurs par catégorie de ventes mensuelles
sellers_by_category = df.groupby('Monthly Sales Category')['Number of Active Sellers'].sum()

# Création du graphique à barres
sellers_by_category.plot(kind='bar')

# Configuration des labels et des titres
plt.xlabel('Catégories de ventes mensuelles')
plt.ylabel('Nombre de vendeurs')
plt.title('Nombre de vendeurs par catégorie de ventes mensuelles')

# Affichage du graphique
plt.show()

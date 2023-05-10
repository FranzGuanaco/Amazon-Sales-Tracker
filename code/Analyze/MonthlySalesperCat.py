import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Analyze/AMZ_Data_Clean.csv')
unique = df['Category'].unique()

monthlysales_per_category = []
for sales in unique:
    sale = df.loc[df['Category']==sales, 'Monthly Sales']
    total = sale.sum()
    num_rows = sale.shape[0]
    avg_sales = round(total / num_rows, 1)
    monthlysales_per_category.append(avg_sales)

sorted_categories, sorted_avg_sales = zip(*sorted(zip(unique, monthlysales_per_category), key=lambda x: x[1], reverse=True))

# Création du graphique
plt.bar(sorted_categories, sorted_avg_sales)

# Configuration des labels et des titres
plt.xlabel('Catégories')
plt.ylabel('Moyenne de vente mensuelle (en dollars)')
plt.title('Moyenne de vente pour chaque catégorie')
plt.xticks(rotation=90)

# Affichage du graphique
plt.show()


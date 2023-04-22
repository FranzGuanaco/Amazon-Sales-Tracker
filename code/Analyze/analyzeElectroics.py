import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Analyze/AMZ_Data_Clean.csv')

focus = df.loc[:, ['Number of Images', 'Category']]
focus = focus.sort_values('Number of Images', ascending=False)

electronics = df.loc[df['Category'] == 'Electronics', ['Number of Images']]

total_images = df['Number of Images'].sum()
num_rows = df.shape[0]

avg_images_per_row = round(total_images / num_rows, 1)

categories = ['Electronics']
category_counts = avg_images_per_row
# Création du graphique
plt.bar(categories, category_counts)
# Configuration des labels et des titres
plt.xlabel('Images')
plt.ylabel('Moyenne de nombre d\'images par produit')
plt.title('Moyenne de nombre d\'images par produit pour chaque catégorie')

# Affichage du graphique
plt.show()

print("Moyenne d'images par ligne: ", avg_images_per_row)








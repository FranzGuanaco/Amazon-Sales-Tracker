import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Analyze/AMZ_Data_Clean.csv')

note = [1, 2, 3, 4, 5]
labels = ['1-2', '2-3', '3-4', '4-5']

df['Review'] = pd.cut(df['Reviews Rating'], bins=note, labels=labels)
group = df.groupby ('Review') ['Monthly Sales'].sum()

group.plot(kind='bar')

# Configuration des labels et des titres
plt.xlabel('Catégories de ventes mensuelles')
plt.ylabel('Nombre de vendeurs')
plt.title('Nombre de vendeurs par catégorie de ventes mensuelles')

# Affichage du graphique
plt.show()



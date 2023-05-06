import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Analyze/AMZ_Data_Clean.csv')

df['Reviews Rating'] = df['Reviews Rating'].dropna()
unique_values = df['Reviews Rating'].unique()
sorted_unique_values = sorted([x for x in unique_values if pd.notna(x)])

average_prices = {}

for note in sorted_unique_values:
    prices_for_note = df.loc[df['Reviews Rating'] == note, 'Price']
    average_price = prices_for_note.mean()
    average_prices[note] = average_price

# Afficher les moyennes des prix pour chaque note
for note, avg_price in average_prices.items():
    print(f"Note {note}: Moyenne des prix = {avg_price}")

# Tracé du graphique à barres
plt.scatter(average_prices.keys(), average_prices.values())

# Configuration des étiquettes et du titre
plt.xlabel('Notes')
plt.ylabel('Prix moyen')
plt.title('Prix moyen par note')

# Affichage du graphique
plt.show()
print(sorted_unique_values[1])

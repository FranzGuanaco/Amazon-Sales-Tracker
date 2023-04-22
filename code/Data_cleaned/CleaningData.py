import pandas as pd

df = pd.read_csv('Data_cleaned/Amz Full Data.csv')
df = df.drop(columns=['Variation Count', 'Height', 'Length', 'Width', 'Size Tier', 'Weight', 'BSR', 'Sales to Reviews', 'Price Trend (90 days) (%)', 'Last Year Sales'])
df = df.drop_duplicates(subset=['URL'])
df = df.drop(columns=['URL'])
df.reset_index(drop=True, inplace=True)
df = df.sort_values('Monthly Sales', ascending=False)

# Trouver les cases vides dans toutes les colonnes
columns = df.columns[df.isnull().any()]

# Afficher le nombre de cases vides pour chaque colonne
print(df[columns].isnull().sum())

print(df[['Monthly Sales']].head())
print(df.shape)


df.to_csv('AMZ_Data_Clean.csv', index=False)



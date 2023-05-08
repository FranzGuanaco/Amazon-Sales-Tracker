import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Analyze/AMZ_Data_Clean.csv')

seller = df['Reviews Rating'].max()

print(seller)
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Analyze/AMZ_Data_Clean.csv')

focus = df.loc[:, ['Number of Images', 'Category']]
focus = focus.sort_values('Number of Images', ascending=False)

print(focus)



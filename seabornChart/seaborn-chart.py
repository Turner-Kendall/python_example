import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_json('trending-data.json')
df['score'] = round ((df.select_dtypes(include='number').sum(axis=1)) /10, 2)
col_min = df['score'].min()
col_max = df['score'].max()
new_min = 1
new_max = 100
df['rank'] = round(((df['score'] - col_min) / (col_max - col_min)) * (new_max - new_min) + new_min, 2)
df_sorted = df.sort_values(by='rank', ascending=False)
last_column = df_sorted.columns[-1]
df = df_sorted[[last_column] + [col for col in df_sorted if col != last_column]]
df = df.drop(columns=['score'])
Terms = df['Term']
t = df.columns.tolist()
ColList=t[2:]
df_long = pd.melt(df, id_vars=['rank', 'Term'], var_name='Date', value_name='Value')
df_long['Date'] = pd.to_datetime(df_long['Date'])  # Convert the 'Date' column to datetime format

sns.set_style('darkgrid')
plt.figure(figsize=(12, 6))
sns.boxplot(x='Term', y='Value',  hue='rank', data=df_long, palette='bright', )
plt.title('Distribution of Terms')
plt.show()
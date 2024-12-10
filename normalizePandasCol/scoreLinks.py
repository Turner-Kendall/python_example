import pandas as pd

df = pd.read_csv('links.csv')

# This just makes the "scores" a manageable size to normalize
df['linkScore'] = df['score'] * .0001

# Which column to normalize (linkScore or score)
s_col = 'linkScore'

# Get the min and max of the column
col_min = df[s_col].min()
col_max = df[s_col].max()
# Set what the new min and max should be
new_min = 1
new_max = 100

# Normalize the column
df['newScore'] = round(((df[s_col] - col_min) / (col_max - col_min)) * (new_max - new_min) + new_min, 2)

# Drop the old score column(s) and rename the remaining ones
df = df.drop(columns=['score','linkScore'])
df.columns = ['url', 'text', 'user', 'timestamp', 'keyword', 'score']

print(df.head())
print(df.tail())
df.to_csv('sorted_links.csv', index=False)

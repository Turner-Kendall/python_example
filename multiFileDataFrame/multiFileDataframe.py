import pandas as pd
import os

# Specify the directory containing your JSON files
directory_path = './test'

# Initialize an empty DataFrame to store the data
df = pd.DataFrame()

# Iterate over all files in the directory 
# Add them to the dataframe
for filename in os.listdir(directory_path):
  if filename.endswith('.json'):
    file_path = os.path.join(directory_path, filename)
    print('Reading file {}'.format(file_path))

    # Read JSON file and append to the DataFrame
    json_data = pd.read_json(file_path, orient='records', lines=True)

    # I think Append is deprecated...
    df = df.append(json_data, ignore_index=True)
    print (f'added {len(json_data)} rows to df, which now has {len(df)} rows')

print(df.head())

# Write the DataFrame to a CSV file
df.to_csv('batch.csv', index=False)
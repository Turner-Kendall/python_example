import os
import json

# This file adds a 'keyword' field to each record in the JSON file
# The 'keyword' field is the name of the file (without the '.json' extension)

directory = './data'

for filename in os.listdir(directory):
  if filename.endswith('.json'):
    file_path = os.path.join(directory, filename)
    with open(file_path, 'r+') as file:
        data = json.load(file)
        
        # Add 'keyword' field to each record in the JSON file
        for record in data:
          # Remove the '.json' extension from the filename
          print(filename[:-5])
          record['keyword'] = filename[:-5]
        
        # Don't forget - Move file pointer to the beginning of the file
        file.seek(0)
        
        json.dump(data, file, indent=4)
        file.truncate()
          
    print(f'Updated {filename} with the "keyword" field.')


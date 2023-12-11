import pandas as pd

# Read the CSV file
csv_file = 'data1.csv'
df = pd.read_csv(csv_file)

# Convert the DataFrame to JSON
json_data = df.to_json(orient='records')

# Save the JSON data to a file
json_file = 'data1.json'
with open(json_file, 'w') as f:
    f.write(json_data)

print(f'CSV file "{csv_file}" has been converted to JSON: "{json_file}"')

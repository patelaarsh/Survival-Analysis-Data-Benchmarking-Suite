# import csv
# import uuid

# # Step 1: Define the CSV file paths
# input_csv_file = 'questdb.csv'
# output_csv_file = 'cassandra.csv'

# # Step 2: Read the CSV file
# with open(input_csv_file, 'r') as input_file:
#     csv_reader = csv.reader(input_file)
#     data = list(csv_reader)

# # Step 3: Generate UUIDs
# uuid_column = [str(uuid.uuid4()) for _ in range(len(data))]

# # Step 4: Add the UUIDs to a new column
# for i, row in enumerate(data):
#     if i == 0:
#         row.append('UUID')  # Add a header for the new column
#     else:
#         row.append(uuid_column[i - 1])

# # Step 5: Write the updated data back to the CSV file
# with open(output_csv_file, 'w', newline='') as output_file:
#     csv_writer = csv.writer(output_file)
#     csv_writer.writerows(data)

# print(f"UUIDs added and saved to {output_csv_file}")

import csv
import uuid

# Step 1: Define the CSV file paths
input_csv_file = 'data1.csv'
output_csv_file = 'cassandra_data1.csv'

# Step 2: Read the CSV file
with open(input_csv_file, 'r') as input_file:
    csv_reader = csv.reader(input_file)
    data = list(csv_reader)

# Step 3: Generate UUIDs
uuid_column = [str(uuid.uuid4()) for _ in range(len(data))]

# Step 4: Insert the UUIDs as the first column
for i, row in enumerate(data):
    if i == 0:
        row.insert(0, 'UUID')  # Add a header for the new column as the first element
    else:
        row.insert(0, uuid_column[i - 1])

# Step 5: Write the updated data back to the CSV file
with open(output_csv_file, 'w', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    csv_writer.writerows(data)

print(f"UUIDs added and saved to {output_csv_file}")

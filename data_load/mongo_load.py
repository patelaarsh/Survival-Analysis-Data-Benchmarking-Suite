import argparse
import pymongo
import json
import time  

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Load JSON data into MongoDB.')
parser.add_argument('--host', type=str, default='localhost', help='MongoDB host address')
parser.add_argument('--port', type=int, default=27017, help='MongoDB port number')
parser.add_argument('--database', type=str, required=True, help='MongoDB database name')
parser.add_argument('--collection', type=str, required=True, help='MongoDB collection name')
parser.add_argument('--json_file', type=str, required=True, help='Path to the JSON file')
args = parser.parse_args()

# Connect to MongoDB
client = pymongo.MongoClient(args.host, args.port)
db = client[args.database]
collection = db[args.collection]

# Record the start time
start_time = time.time()

# Load JSON data into MongoDB
with open(args.json_file, 'r') as json_file:
    data = json.load(json_file)
    if isinstance(data, list):
        collection.insert_many(data)
        print(f'{len(data)} documents inserted into {args.collection} in {args.database}.')
    elif isinstance(data, dict):
        collection.insert_one(data)
        print(f'1 document inserted into {args.collection} in {args.database}.')
    else:
        print('Invalid JSON data format.')

# Record the end time
end_time = time.time()

# Calculate and print the elapsed time
elapsed_time = end_time - start_time
print(f'Data loading took {elapsed_time:.2f} seconds.')

# Close the MongoDB connection
client.close()

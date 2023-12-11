import pymongo
import time

# Replace with your MongoDB connection details
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["project2"]
collection = db["data"]

# Start timing
start_time = time.time()

# Define the filter to count the number of documents with the boolean column set to True
filter_true = {'is_dead': True}

# Count the number of documents with True values
true_count = collection.count_documents(filter_true)

# Count the total number of documents in the collection
total_count = collection.count_documents({})

# Calculate the percentage of True values
if total_count > 0:
    percentage_true = (true_count / total_count) * 100
    print(f"Percentage of True values: {percentage_true:.2f}%")

# Close the MongoDB connection
client.close()

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution Time: {execution_time:.2f} seconds")



import pymongo
import time

# Replace with your MongoDB connection details
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["project1"]
collection = db["data"]

# Start timing
start_time = time.time()

# Define the aggregation pipeline
pipeline = [
    {
        "$match": {
            "date_start_observed": {"$gt": "1991-09-10T00:00:00Z"},
            "date_end_observed": {"$lt": "2010-03-07T00:00:00Z"},
            "is_dead": True
        }
    },
    {
        "$group": {
            "_id": None,
            "count": {"$sum": 1}
        }
    }
]

# Execute the aggregation pipeline and retrieve the result
result = list(collection.aggregate(pipeline))

# Extract the count from the result
count = result[0]["count"]

# Print the count
print("Count:", count)

# Close the MongoDB connection
client.close()

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution Time: {execution_time:.2f} seconds")



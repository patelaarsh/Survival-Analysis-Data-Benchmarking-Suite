import pymongo
import time

# Replace with your MongoDB connection details
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["project2"]
collection = db["data"]

# Start timing
start_time = time.time()

pipeline = [
    {
        "$match": { "is_censored": False }
    },
    {
        "$project": {
            "duration": { "$subtract": ["$age_end", "$age_start_observed"] }
        }
    },
    {
        "$group": {
            "_id": None,
            "average_duration_of_observation": { "$avg": "$duration" }
        }
    }
]

# Execute the aggregation pipeline and retrieve the result
result = list(collection.aggregate(pipeline))
print("average_duration_of_observation:", result[0]["average_duration_of_observation"])

# Close the MongoDB connection
client.close()

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution Time: {execution_time:.2f} seconds")



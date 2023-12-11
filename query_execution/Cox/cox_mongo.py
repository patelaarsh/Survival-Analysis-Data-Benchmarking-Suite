import time
import pandas as pd
from pymongo import MongoClient
from lifelines import CoxPHFitter
import lifelines as lf
from lifelines.statistics import logrank_test

# Connect to your MongoDB instance (replace with your MongoDB connection details)
client = MongoClient('mongodb://localhost:27017/')

# Specify the collection where your data is stored (replace with your collection name)
collection = client.project1.data

start_time = time.time()

# data = pd.DataFrame(list(collection.find()))

# query = {
#     "age_start_observed": {"$exists": True},
#     "age_end": {"$exists": True},
#     "is_truncated": {"$exists": True},
#     "is_dead": {"$exists": True}
# }

# Query the data from MongoDB and store it in a DataFrame
mogDB = list(collection.find(projection={'_id': False, 'date_start_observed': False, 'date_end_observed': False,'is_censored': False}))
data = pd.DataFrame(mogDB)

# Create a CoxPHFitter object
model = CoxPHFitter()

# Specify the columns for duration and event
#duration_col = data['age_end']  # Replace with your duration column name
#event_col = data['is_dead']    # Replace with your event column name

model.fit(data, duration_col='age_end', event_col='is_dead')

# Fit the Cox proportional hazards model to the data
#model.fit(data, duration_col=duration_col, event_col=event_col)

# Display the summary of the Cox regression model
# summary = model.summary
# print(summary)

model.print_summary()


# Visualize the survival curves
#model.plot()

# Record the execution time
execution_time = time.time() - start_time

# Print the execution time
print(f"Execution time: {execution_time:.2f} seconds")

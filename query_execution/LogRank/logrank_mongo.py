import pandas as pd
from lifelines import CoxPHFitter
from pymongo import MongoClient
import lifelines as lf
from lifelines.statistics import logrank_test
import time

# Connect to your MongoDB instance (replace with your MongoDB connection details)
client = MongoClient('mongodb://localhost:27017/')

# Specify the collection where your data is stored (replace with your collection name)
collection = client.project2.data

start_time = time.time()

# Query the data from MongoDB and store it in a DataFrame
data = pd.DataFrame(list(collection.find()))

# # Create a CoxPHFitter object
# model = CoxPHFitter()

# # Specify the columns for duration and event
# duration_col = 'age_end'  # Replace with your duration column name
# event_col = 'is_dead'    # Replace with your event column name

# # Fit the Cox proportional hazards model to the data
# model.fit(data, duration_col=duration_col, event_col=event_col)

# Fit the model to the data
# model.fit(data, duration_col='age_end', event_col='is_dead')

# # Display the summary of the Cox regression model
# model.print_summary()

# # Visualize the survival curves
# model.plot()

# Create a KaplanMeierFitter object
kmf = lf.KaplanMeierFitter()

# Fit the model to the data
kmf.fit(data['age_end'], event_observed=data['is_dead'])

# Perform the log-rank test
results = logrank_test(data['is_dead'], data['age_end'])

# Print the results
print(results)

# Record the execution time
execution_time = time.time() - start_time

# Print the execution time
print(f"Execution time: {execution_time:.2f} seconds")


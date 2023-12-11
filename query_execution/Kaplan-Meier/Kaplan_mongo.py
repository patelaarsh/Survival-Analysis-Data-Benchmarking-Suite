import pandas as pd
from lifelines import KaplanMeierFitter
from pymongo import MongoClient
import time

# Connect to your MongoDB instance (replace with your MongoDB connection details)
client = MongoClient('mongodb://localhost:27017/')

# Specify the collection where your data is stored (replace with your collection name)
collection = client.project2.data

start_time = time.time()

# Query the data from MongoDB and store it in a DataFrame
data = pd.DataFrame(list(collection.find()))

# Calculate time-to-event
data['time_to_event'] = data['age_end'] - data['age_start_observed']

# Set event status based on 'is_dead' and 'is_censored'
data['event_status'] = data['is_dead'].apply(lambda x: 1 if x else 0)
data.loc[data['is_censored'], 'event_status'] = 0

# Perform Kaplan-Meier analysis
kmf = KaplanMeierFitter()
kmf.fit(data['time_to_event'], event_observed=data['event_status'])

# Calculate the median survival time
median_survival_time = kmf.median_survival_time_

# Record the execution time
execution_time = time.time() - start_time

# Print the median survival time
print(f"Median Survival Time: {median_survival_time}")

# Print the execution time
print(f"Execution time: {execution_time:.2f} seconds")

# Plot the Kaplan-Meier curve
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
kmf.plot(label="Kaplan-Meier Estimate")
plt.xlabel("Time")
plt.ylabel("Survival Probability")
plt.title("Kaplan-Meier Survival Curve")
plt.show()


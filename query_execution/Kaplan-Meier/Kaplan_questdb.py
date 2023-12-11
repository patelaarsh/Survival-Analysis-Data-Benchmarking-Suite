import pandas as pd
import numpy as np
from lifelines import KaplanMeierFitter
import matplotlib.pyplot as plt
import httpx
import time

# Define the QuestDB REST API endpoint (replace with your QuestDB endpoint)
questdb_url = 'http://localhost:9000'

# Specify the SQL query to retrieve the data
sql_query = "SELECT age_start_observed, age_end, is_dead, is_censored FROM project2"

# Record the start time
start_time = time.time()

# Execute the SQL query using QuestDB's REST API
with httpx.Client() as client:
    response = client.get(f"{questdb_url}/exec?query={sql_query}")
    data = response.json()

#print(data)

# Create a DataFrame from the retrieved data
data = pd.DataFrame(data['dataset'])

# Calculate time-to-event
data['time_to_event'] = data[1] - data[0]
#print(data('age_end'))

# Set event status based on 'is_dead' and 'is_censored'
data['event_status'] = np.where(data[2], 1, 0)
data.loc[data[3], 'event_status'] = 0

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
plt.figure(figsize=(10, 6))
kmf.plot(label="Kaplan-Meier Estimate")
plt.xlabel("Time")
plt.ylabel("Survival Probability")
plt.title("Kaplan-Meier Survival Curve")
plt.show()

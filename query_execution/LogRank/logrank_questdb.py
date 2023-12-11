import pandas as pd
import numpy as np
import lifelines as lf
from lifelines.statistics import logrank_test
from lifelines import CoxPHFitter, KaplanMeierFitter
import matplotlib.pyplot as plt
import httpx
import time

# Define the QuestDB REST API endpoint (replace with your QuestDB endpoint)
questdb_url = 'http://localhost:9000'

# Specify the SQL query to retrieve the data
sql_query = "SELECT age_start_observed, age_end, is_dead, is_truncated FROM project1"

# Record the start time
start_time = time.time()

# Execute the SQL query using QuestDB's REST API
with httpx.Client() as client:
    response = client.get(f"{questdb_url}/exec?query={sql_query}")
    data = response.json()

# Create a DataFrame from the retrieved data
data = pd.DataFrame(data['dataset'])

kmf = lf.KaplanMeierFitter()

# Fit the model to the data
kmf.fit(data[1], event_observed=data[2])

# Perform the log-rank test
results = logrank_test(data[1], data[2])

# Print the results
print(results)

# Record the execution time
execution_time = time.time() - start_time

# Print the execution time
print(f"Execution time: {execution_time:.2f} seconds")



# print(data)

# Create a CoxPHFitter object
# model = CoxPHFitter()

# duration = data[1]
# event = data[2]
# model.fit(data, duration_col=duration, event_col=event)

# # Display the summary of the Cox regression model
# model.print_summary()

# # Visualize the survival curves
# model.plot()

# Specify the correct column names for duration and event
# duration_col = 'age_end'  # Replace with the correct column name for duration
# event_col = 'is_dead'    # Replace with the correct column name for the event

# # Ensure the data types are appropriate (e.g., duration as float, event as boolean)
# data[duration_col] = data[duration_col].astype(float)
# data[event_col] = data[event_col].astype(bool)

# # Create a CoxPHFitter object
# model = CoxPHFitter()

# # Fit the Cox proportional hazards model to the data
# model.fit(data, duration_col=duration_col, event_col=event_col)

# # Display the summary of the Cox regression model
# model.print_summary()

# # Visualize the survival curves
# model.plot()


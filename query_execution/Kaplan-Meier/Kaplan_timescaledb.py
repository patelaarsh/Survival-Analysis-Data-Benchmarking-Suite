import pandas as pd
import lifelines as lf
from lifelines import KaplanMeierFitter
from lifelines import CoxPHFitter
from lifelines.statistics import logrank_test
import psycopg2
import time

# Replace with your TimeScaleDB connection details
conn = psycopg2.connect(
    host="localhost",
    database="aarsh",
    user="postgres",
    password="aarsh"
)

# Specify your SQL query to retrieve data (replace with your query)
query = "SELECT age_start_observed, age_end, is_truncated, is_censored, is_dead FROM data2"

start_time = time.time()

# Retrieve data from TimescaleDB and store it in a DataFrame
data = pd.read_sql_query(query, conn)

# # Create a KaplanMeierFitter object
# kmf = lf.KaplanMeierFitter()

# # Fit the model to the data
# kmf.fit(data['age_end'], event_observed=data['is_dead'])

# # Perform the log-rank test
# results = logrank_test(data['is_dead'], data['age_end'], data['is_truncated'])

# Print the results
#print(results)

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

# Close the database connection
conn.close()


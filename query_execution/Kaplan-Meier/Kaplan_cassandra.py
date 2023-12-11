import pandas as pd
from lifelines import KaplanMeierFitter
import time
from cassandra.cluster import Cluster,ExecutionProfile, EXEC_PROFILE_DEFAULT

execprof = ExecutionProfile(request_timeout=1000000000)
profiles = {EXEC_PROFILE_DEFAULT:execprof}

# Connect to Cassandra (replace with your connection details)
cluster = Cluster(['localhost'], execution_profiles=profiles)
session = cluster.connect('project2')

# Specify your CQL query to retrieve data (replace with your query)ython 
query = "SELECT age_start_observed, age_end, is_truncated, is_censored, is_dead FROM data ALLOW FILTERING"

start_time = time.time()

# Retrieve data from Cassandra and store it in a DataFrame
result_data = []
for user_row in session.execute(query):
    result_data.append(user_row)

data = pd.DataFrame(result_data)

# Calculate time-to-event
data['time_to_event'] = data['age_start_observed'] - data['age_end']

# Set event status based on 'is_dead' and 'is_censored'
data['event_status'] = data['is_truncated'].apply(lambda x: 1 if x else 0)
data.loc[data['is_dead'], 'event_status'] = 0

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


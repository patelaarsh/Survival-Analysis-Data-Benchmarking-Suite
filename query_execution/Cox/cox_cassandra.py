import pandas as pd
import time
import lifelines as lf
from lifelines import CoxPHFitter
from lifelines.statistics import logrank_test
import matplotlib.pyplot as plt
from cassandra.cluster import Cluster,ExecutionProfile, EXEC_PROFILE_DEFAULT
from cassandra.query import dict_factory

execprof = ExecutionProfile(request_timeout=100000,row_factory=dict_factory)
profiles = {EXEC_PROFILE_DEFAULT:execprof}

# Connect to Cassandra (replace with your connection details)
cluster = Cluster(['localhost'], execution_profiles=profiles)
session = cluster.connect('project1')

# Specify your SQL query to retrieve data (replace with your query)
query = "SELECT age_start_observed,age_end,is_truncated,is_censored FROM data"

start_time = time.time()

# Retrieve data from Cassandra and store it in a DataFrame
# statement = SimpleStatement(query, fetch_size=50)
# results = session.execute(statement)

# # save page state
# page_state = results.paging_state

# count = 0
# for data in results:
#     count += 1
      
# print("Count:" , count)
result_data = []
for user_row in session.execute(query):
    result_data.append(user_row)

data = pd.DataFrame(result_data)

model = CoxPHFitter()

model.fit(data, duration_col='age_start_observed', event_col='is_truncated')


# Display the summary of the Cox regression model
model.print_summary()

# Record the execution time
execution_time = time.time() - start_time

# Print the execution time
print(f"Execution time: {execution_time:.2f} seconds")

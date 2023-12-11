import pandas as pd
from lifelines import CoxPHFitter
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

model = CoxPHFitter()

model.fit(data, duration_col=1, event_col=2)
model.print_summary()

# Record the execution time
execution_time = time.time() - start_time

# Print the execution time
print(f"Execution time: {execution_time:.2f} seconds")

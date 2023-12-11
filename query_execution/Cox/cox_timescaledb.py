import pandas as pd
from lifelines.statistics import logrank_test
from lifelines import CoxPHFitter
import psycopg2
import time
import lifelines as lf


# Replace with your TimeScaleDB connection details
conn = psycopg2.connect(
    host="localhost",
    database="aarsh",
    user="postgres",
    password="aarsh"
)

# Specify your SQL query to retrieve data (replace with your query)
query = "SELECT age_start_observed,age_end,is_truncated,is_dead FROM data1"

start_time = time.time()

# Execute the SQL query and load the data into a DataFrame
data = pd.read_sql_query(query, conn)

#Create a CoxPHFitter object
model = CoxPHFitter()

model.fit(data, duration_col='age_end', event_col='is_dead')

# Display the summary of the Cox regression model
model.print_summary()

# Record the execution time
execution_time = time.time() - start_time

# Print the execution time
print(f"Execution time: {execution_time:.2f} seconds")

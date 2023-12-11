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

# Specify your SQL query to retrieve data
query = "SELECT age_start_observed,age_end,is_truncated,is_dead FROM data1"

# Execute the SQL query and load the data into a DataFrame
data = pd.read_sql_query(query, conn)

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


#Create a CoxPHFitter object
# model = CoxPHFitter()

# model.fit(df, duration_col='age_end', event_col='is_dead')

# # Display the summary of the Cox regression model
# model.print_summary()

# # Visualize the survival curves
# model.plot()
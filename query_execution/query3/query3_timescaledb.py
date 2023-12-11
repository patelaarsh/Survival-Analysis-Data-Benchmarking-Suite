import psycopg2
import time

# Replace with your TimeScaleDB connection details
conn = psycopg2.connect(
    host="localhost",
    database="aarsh",
    user="postgres",
    password="aarsh"
)

# Start timing
start_time = time.time()

query="SELECT AVG(age_end - age_start_observed) AS average_duration_of_observation FROM data2 WHERE is_censored = False"

cur = conn.cursor()
cur.execute(query)
result = cur.fetchall()

# Print the data (for demonstration purposes)
for row in result:
    print(row)

# Calculate and print execution time
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution Time: {execution_time:.2f} seconds")

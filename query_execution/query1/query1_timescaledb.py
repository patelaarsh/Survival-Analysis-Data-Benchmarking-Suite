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

query="SELECT COUNT(*) FROM data1 WHERE date_start_observed > '1991-09-10' AND date_end_observed < '2010-03-07' AND is_dead = true"

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

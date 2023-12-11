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

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Define the SQL query to count the number of True values in the boolean column
sql_query = """
    SELECT COUNT(*) FROM data2 WHERE is_dead = TRUE;
"""

# Execute the SQL query
cursor.execute(sql_query)

# Fetch the result (count of True values)
true_count = cursor.fetchone()[0]

# Define the SQL query to count the total number of rows in the table
sql_query_total = """
    SELECT COUNT(*) FROM data2;
"""

# Execute the SQL query
cursor.execute(sql_query_total)

# Fetch the result (total count)
total_count = cursor.fetchone()[0]

# Calculate the percentage of True values
if total_count > 0:
    percentage_true = (true_count / total_count) * 100
    print(f"Percentage of True values: {percentage_true:.2f}%")

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution Time: {execution_time:.2f} seconds")

# Close the cursor and the database connection
cursor.close()
conn.close()


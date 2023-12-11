from cassandra.cluster import Cluster, ExecutionProfile, EXEC_PROFILE_DEFAULT
import time

# Replace with your Cassandra cluster contact points and keyspace

execprof = ExecutionProfile(request_timeout=100000)
profiles = {EXEC_PROFILE_DEFAULT:execprof}
cluster = Cluster(['localhost'], execution_profiles=profiles)
session = cluster.connect('project2')

# Start timing
start_time = time.time()

# Define the CQL query to count the number of True values in the boolean column
cql_query = f"SELECT COUNT(*) FROM data WHERE is_truncated = true ALLOW FILTERING"

# Execute the CQL query
result = session.execute(cql_query)

# Fetch the count of True values
true_count = result.one()[0]

# Define the CQL query to count the total number of rows in the table
cql_query_total = f"SELECT COUNT(*) FROM data ALLOW FILTERING"

# Execute the CQL query
result_total = session.execute(cql_query_total)

# Fetch the total count
total_count = result_total.one()[0]

# Calculate the percentage of True values
if total_count > 0:
    percentage_true = (true_count / total_count) * 100
    print(f"Percentage of True values: {percentage_true:.2f}%")

# Close the Cassandra cluster connection
cluster.shutdown()

# Calculate and print execution time
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution Time: {execution_time:.2f} seconds")

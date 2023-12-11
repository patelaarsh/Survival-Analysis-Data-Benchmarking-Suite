from cassandra.cluster import Cluster, ExecutionProfile, EXEC_PROFILE_DEFAULT
import time

# Replace with your Cassandra cluster contact points and keyspace

execprof = ExecutionProfile(request_timeout=100000)
profiles = {EXEC_PROFILE_DEFAULT:execprof}
cluster = Cluster(['localhost'], execution_profiles=profiles)
session = cluster.connect('project1')

start_time = time.time()

query = """
    SELECT COUNT(*)
    FROM data1
    WHERE date_start_observed > '1991-09-10'
        AND date_end_observed < '2010-03-07'
        AND is_dead = true
    ALLOW FILTERING
"""
result = session.execute(query)

# Print the data (for demonstration purposes)
for row in result:
    print(row)

# Calculate and print execution time
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution Time: {execution_time:.2f} seconds")




from cassandra.cluster import Cluster, ExecutionProfile, EXEC_PROFILE_DEFAULT
import time

execprof = ExecutionProfile(request_timeout=100000)
profiles = {EXEC_PROFILE_DEFAULT:execprof}
cluster = Cluster(['localhost'], execution_profiles=profiles)
session = cluster.connect('project2')

start_time = time.time()

query="SELECT AVG(age_end - age_start_observed) AS average_duration_of_observation FROM data WHERE is_dead = False ALLOW FILTERING;"

result = session.execute(query)

for row in result:
    print(row)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution Time: {execution_time:.2f} seconds")




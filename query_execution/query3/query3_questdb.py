import requests
import time
import urllib.parse

start_time = time.time()

query="SELECT AVG(age_end - age_start_observed) AS average_duration_of_observation FROM project2 WHERE is_censored = False;"
encoded_query = urllib.parse.quote(query)
url = f'http://localhost:9000/exp?query={encoded_query}'

resp = requests.get(url)

print(resp.text)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution Time: {execution_time:.2f} seconds")


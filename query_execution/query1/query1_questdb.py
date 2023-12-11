import requests
import time
import urllib.parse

start_time = time.time()

query = """
    SELECT COUNT(*)
    FROM project1
    WHERE date_start_observed > '1991-09-10'
        AND date_end_observed < '2010-03-07'
        AND is_dead = true
"""
encoded_query = urllib.parse.quote(query)
url = f'http://localhost:9000/exp?query={encoded_query}'

resp = requests.get(url)
print(resp.text)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution Time: {execution_time:.2f} seconds")


import requests
import time
import urllib.parse

start_time = time.time()

query1 = "SELECT COUNT(*) FROM project2 WHERE is_dead = TRUE"
encoded_query1 = urllib.parse.quote(query1)
url1 = f'http://localhost:9000/exp?query={encoded_query1}'

resp1 = requests.get(url1)

query2 = "SELECT COUNT(*) FROM project2"
encoded_query2 = urllib.parse.quote(query2)
url2 = f'http://localhost:9000/exp?query={encoded_query2}'

resp2 = requests.get(url2)

# Extract numerical values from the response texts
count_true = int(resp1.text.split('\n')[1].strip())  
count_total = int(resp2.text.split('\n')[1].strip()) 

# Calculate the percentage of True values
if count_total > 0:
    percentage_true = (count_true / count_total) * 100
else:
    percentage_true = 0

print(f"Percentage of True values: {percentage_true:.2f}%")

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution Time: {execution_time:.2f} seconds")

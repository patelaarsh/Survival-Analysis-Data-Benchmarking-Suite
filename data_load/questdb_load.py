import sys
import requests
import time

# Check if the correct number of arguments are provided
if len(sys.argv) != 4:
    print("Usage: python script.py host table_name data_file")
    sys.exit(1)

# Command-line arguments
host = sys.argv[1]
table_name = sys.argv[2]
data_file_path = sys.argv[3]

try:
    with open(data_file_path, 'r') as data_file:
        csv = {'data': (table_name, data_file)}

        # Record the start time
        start_time = time.time()

        response = requests.post(host + '/imp', files=csv)

        # Record the end time
        end_time = time.time()
        
        print(f'Data loaded into {table_name}')
        print(f'Data loading took {end_time - start_time:.2f} seconds.')
except FileNotFoundError:
    print(f"Error: File '{data_file_path}' not found.", file=sys.stderr)
except requests.exceptions.RequestException as e:
    print(f'Error: {e}', file=sys.stderr)
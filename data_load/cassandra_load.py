import argparse
from cassandra.cluster import Cluster
import subprocess
import time

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Create Cassandra keyspace and table.')
parser.add_argument('--host', type=str, default='localhost', help='Comma-separated list of Cassandra host addresses')
parser.add_argument('--port', type=int, default=9042, help='Cassandra port number')
parser.add_argument('--keyspace', type=str, required=True, help='Cassandra keyspace name')
parser.add_argument('--table', type=str, required=True, help='Cassandra table name')
parser.add_argument('--csv_file', type=str, required=True, help='Path to the CSV file')
args = parser.parse_args()

# Connect to Cassandra
print(args.host)
cluster = Cluster([args.host], port=args.port)
session = cluster.connect()

# Create the keyspace if it doesn't exist
create_keyspace_query = f"""
    CREATE KEYSPACE IF NOT EXISTS {args.keyspace}
    WITH REPLICATION = {{ 'class' : 'SimpleStrategy', 'replication_factor' :  1}}
"""

session.execute(create_keyspace_query)

# Set the keyspace for further operations
session.set_keyspace(args.keyspace)


# Create the table with the specified schema
create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {args.table} (
        UIUD TEXT PRIMARY kEY,     
        age_start_observed INT,
        age_end INT,
        date_start_observed DATE,
        date_end_observed DATE,
        is_truncated BOOLEAN,
        is_censored BOOLEAN,
        is_dead BOOLEAN
    )
"""

session.execute(create_table_query)

# Record the start time
start_time = time.time()

# Execute the COPY command using cqlsh
copy_command = f"cqlsh -e \"COPY {args.keyspace}.{args.table} FROM '{args.csv_file}' WITH HEADER = true;\""

subprocess.run(copy_command, shell=True)

# Record the end time
end_time = time.time()

# Close the Cassandra connection
session.shutdown()
cluster.shutdown()

# Calculate and print the elapsed time
elapsed_time = end_time - start_time
print(f'Data loading took {elapsed_time:.2f} seconds.')


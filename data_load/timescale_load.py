import argparse
import psycopg2
import csv
import time

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Load CSV data into TimescaleDB.')
parser .add_argument('--host', type=str, default='localhost', help='TimescaleDB host address')
parser.add_argument('--port', type=int, default=5432, help='TimescaleDB port number')
parser.add_argument('--database', type=str, required=True, help='TimescaleDB database name')
parser.add_argument('--table', type=str, required=True, help='TimescaleDB table name')
parser.add_argument('--username', type=str, required=True, help='TimescaleDB username')
parser.add_argument('--password', type=str, required=True, help='TimescaleDB password')
parser.add_argument('--csv_file', type=str, required=True, help='Path to the CSV file')
args = parser.parse_args()

# TimescaleDB connection parameters (without specifying the database)
db_params_without_db = {
    'host': args.host,
    'port': args.port,
    'user': args.username,
    'password': args.password
}

# Record the start time
start_time = time.time()

try:
    # Create a connection without specifying a database
    connection = psycopg2.connect(**db_params_without_db)
    cursor = connection.cursor()

    # Check if the database exists
    cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{args.database}'")
    if not cursor.fetchone():
        # Database doesn't exist, so create it
        cursor.execute(f"CREATE DATABASE {args.database}")
        connection.commit()

    # Close the initial connection
    cursor.close()
    connection.close()

    # Connect to the specified database
    db_params = db_params_without_db.copy()
    db_params['dbname'] = args.database
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Read the CSV file to get the column names
    with open(args.csv_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)

    # Create the table if it doesn't exist, dynamically generating the schema
    create_table_query = f"CREATE TABLE IF NOT EXISTS {args.table} ("
    for column_name in header:
        create_table_query += f"{column_name} TEXT, "
    create_table_query = create_table_query.rstrip(', ') + ");"

    cursor.execute(create_table_query)
    connection.commit()

    # Load data from CSV file into the table
    with open(args.csv_file, 'r') as csv_file:
        cursor.copy_expert(f"COPY {args.table} FROM STDIN CSV HEADER DELIMITER ','", csv_file)
        connection.commit()

    print(f'Data loaded into {args.table} in {args.database}.')

except (Exception, psycopg2.Error) as error:
    print('Error:', error)

finally:
    # Close the TimescaleDB connection
    if connection:
        cursor.close()
        connection.close()

# Record the end time
end_time = time.time()

# Calculate and print the elapsed time
elapsed_time = end_time - start_time
print(f'Data loading took {elapsed_time:.2f} seconds.')

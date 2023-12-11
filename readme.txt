To install the required python packages,you can use pip:
pip install time
pip install pymongo
pip install lifelines

Install/Setup Databases :
User Docker Compose. Install Docker
Modify docker-compose.yml if needed (add more databases or edit configurations) 
docker-compose up -d timescaledb
 
Generate Data:
python generate_data.py --n 10000000 --database timescaledb (For CSV format for TimescaleDB, QuestDB)
Convert to JSON using mongodb_json script for MongoDB
Use the cassandra_addColumn script for loading data in Cassandra

Load data in MongoDB :
python mongo_load.py --database survival_data --collection data --json_file survival_data.json

Load Data in TimeScaleDB:
Create the Database manually in the command line or using pgAdmin
python timescale_load.py --database survival_data --table data --csv_file survival_data.csv --username postgres --password aarsh

Load Data in QuestDB:
Start Docker container/docker-compose
Check port 9000 
python questdb_load.py http://localhost:9000 project1 data1.csv

Load Data in Cassandra:
python cassandra_load.py --keyspace project1 --table data --csv_file cassandra_data1.csv

Run Queries:
Modify the database and table name as required and directly run the script files. Example:
'python query1_mongodb.py' will connect to MongoDB, perform the query, and return the results.

Every script for data generation, data loading, and query generation can be changed accordingly.







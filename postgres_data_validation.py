import yaml
import great_expectations as gx

context = gx.get_context()

# Load the YAML file
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

# Access the database credentials
db_creds = config['db_creds']
drivername = db_creds['drivername']
host = db_creds['host']
port = db_creds['port']
username = db_creds['username']
password = db_creds['password']
database = db_creds['database']

# Print the parsed credentials
print("Drivername:", drivername)
print("Host:", host)
print("Port:", port)
print("Username:", username)
print("Password:", password)
print("Database:", database)

connection_string = f"postgres connection: postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"

datasource_name = "my_postgres_datasource"
datasource = context.sources.add_or_update_postgres(
    name=datasource_name
    , connection_string=connection_string
)
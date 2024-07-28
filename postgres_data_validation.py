import os
from dotenv import load_dotenv
import great_expectations as gx

# enable .env file
load_dotenv()

# env variables
username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")
host = os.environ.get("HOST")
port = os.environ.get("PORT")
db = os.environ.get("DATABASE")

# postgres connectionn string
PG_CONNECTION_STRING = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{db}'

# context
context = gx.get_context()

# connect to DB
pg_data_source = context.sources.add_or_update_postgres(
    name="pg_datasource",
    connection_string=PG_CONNECTION_STRING)

# create asset
pg_data_source.add_table_asset(
    name="public_actor_data",
    table_name="public.actor"
)

# create batch request
batch_request = pg_data_source.get_asset("public_actor_data").build_batch_request()

# create expectation
expectation_suite_name = "dvdrental_actor_x_suite"
context.add_or_update_expectation_suite(expectation_suite_name=expectation_suite_name)
validator = context.get_validator(
    batch_request=batch_request,
    expectation_suite_name=expectation_suite_name,
)

# validations
validator.expect_column_values_to_not_be_null(column="actor_id")

# checkpoint
checkpoint = context.add_or_update_checkpoint(
    name="my_postgres_quickstart_checkpoint",
    validator=validator,
)

checkpoint_result = checkpoint.run()
result = dict(checkpoint_result)["_success"]

success_fail = "Success" if result else "Fail"

print(f"Validation: {success_fail}")

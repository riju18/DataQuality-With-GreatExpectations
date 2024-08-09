import pandas as pd
import great_expectations as gx
from great_expectations.core.batch import BatchRequest, RuntimeBatchRequest

# data
data = {
    "name": ["samrat", "max"],
    "profession": ["engineer", "doctor"]
}

# convert to pandas DF
df = pd.DataFrame(data)

# connect to data
context = gx.get_context()
validator = context.sources.pandas_default.read_dataframe(
    dataframe=df
)

# create expectations
validator.expect_column_to_exist(column="id")
validator.save_expectation_suite(discard_failed_expectations=False)

#  create a checkpoint
checkpoint = context.add_or_update_checkpoint(
    name="my_quickstart_checkpoint",
    validator=validator,
)

# validation result
checkpoint_result = checkpoint.run()
result = dict(checkpoint_result)["_success"]
print(f"checkpoint result: {result}")

if result:
    print("data is perfect ...")
else:
    print("data quality is not good")
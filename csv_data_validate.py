import great_expectations as gx

# create data context
context = gx.get_context()

# connect to data
validator = context.sources.pandas_default.read_csv("employee_data.csv")

# create expectations
validator.expect_column_to_exist(column="id")

validator.expect_table_column_count_to_be_between(min_value=1, 
                                        max_value=3)

validator.expect_table_row_count_to_be_between(min_value=1, 
                                               max_value=100)

validator.expect_column_values_to_not_be_null(column="id",
                                              notes="**identification** of each employee")
validator.expect_column_values_to_be_between(
    "id", 
    min_value=1, 
    max_value=10
)

validator.expect_column_values_to_be_unique(column="id")

validator.expect_column_unique_value_count_to_be_between(column="id",
                                                         min_value=1,
                                                         max_value=10)

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
# checkpoint_config

# visualize results as HTML representation
context.view_validation_result(checkpoint_result)  # perfect to visualize the results (not mandatory)
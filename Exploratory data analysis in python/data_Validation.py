# Detecting datatypes....................................................................
# Update the data type of the 2019 column of unemployment to float.
# Print the dtypes of the unemployment DataFrame again to check that the data type has been updated!
# Update the data type of the 2019 column to a float
unemployment["2019"] = unemployment["2019"].astype(float)
# Print the dtypes to check your work
print(unemployment.head())

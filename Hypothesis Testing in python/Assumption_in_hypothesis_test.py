# late_shipments is available, and pandas is loaded as pd.Get the count of each value in the freight_cost_group column of late_shipments.
# Insert a suitable number to inspect whether the counts are "big enough" for a two sample t-test
# Count the freight_cost_group values
counts = late_shipments["freight_cost_group"].value_counts()

# Print the result
print(counts)

# Inspect whether the counts are big enough
print((counts >= 30).all())


# Get the count of each value in the late column of late_shipments.
# Insert a suitable number to inspect whether the counts are "big enough" for a one sample proportion test.

# Count the late values
counts = late_shipments["late"].value_counts()

# Print the result
print(counts)

# Inspect whether the counts are big enough
print((counts >= 10).all())

# Dealing with missing data
# Print the number of missing values in each column of the DataFrame.
# Count the number of missing values in each column
print(planes.isna().sum())

# Calculate how many observations five percent of the planes DataFrame is equal to.
# Count the number of missing values in each column
print(planes.isna().sum())

# Find the five percent threshold
threshold = len(planes) * 0.05

# Create cols_to_drop by applying boolean indexing to columns of the DataFrame with missing values less than or equal to the threshold.
# Use this filter to remove missing values and save the updated DataFrame.

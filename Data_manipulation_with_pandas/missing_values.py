# Print a DataFrame that shows whether each value in avocados_2016 is missing or not.
# Print a summary that shows whether any value in each column is missing or not.
# Create a bar plot of the total number of missing values in each column.

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Check individual values for missing values
print(avocados_2016.isna())


# Check each column for missing values
print(avocados_2016.isna().any())

# Bar plot of missing values by variable
avocados_2016.isna().sum().plot(kind="bar")

# Show plot
plt.show()


# Remove the rows of avocados_2016 that contain missing values and store the remaining rows in avocados_complete.
# Verify that all missing values have been removed from avocados_complete. Calculate each column that has NAs and print.

# Remove rows with missing values
avocados_complete = avocados_2016.dropna()

# Check if any columns contain missing values
print(avocados_complete.isna().any())


# A list has been created, cols_with_missing, containing the names of columns with missing values: "small_sold", "large_sold", and "xl_sold".
# Create a histogram of those columns.
# Show the plot.

# List the columns with missing values
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]

# Create histograms showing the distributions cols_with_missing
avocados_2016[cols_with_missing].hist()

# Show the plot
plt.show()


# Replace the missing values of avocados_2016 with 0s and store the result as avocados_filled.
# Create a histogram of the cols_with_missing columns of avocados_filled.


# From previous step
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
avocados_2016[cols_with_missing].hist()
plt.show()

# Fill in missing values with 0
avocados_filled = avocados_2016.fillna(0)

# Create histograms of the filled columns
avocados_filled[cols_with_missing].hist()

# Show the plot
plt.show()

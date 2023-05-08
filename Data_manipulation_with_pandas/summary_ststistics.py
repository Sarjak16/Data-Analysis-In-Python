# Summary statistics are exactly what they sound like - they summarize many numbers in one statistic. 
# For example, mean, median, minimum, maximum, and standard deviation are summary statistics. 
# Calculating summary statistics allows you to get a better sense of your data, even if there's a lot of it.
# sales is available and pandas is loaded as pd.:
 # question
#   Explore your new DataFrame first by printing the first few rows of the sales DataFrame.
# Print information about the columns in sales.
# Print the mean of the weekly_sales column.
# Print the median of the weekly_sales column.

# Print the head of the sales DataFrame
print(sales.head())

# Print the info about the sales DataFrame
print(sales.info())

# Print the mean of weekly_sales
print(sales['weekly_sales'].mean())

# Print the median of weekly_sales
print(sales['weekly_sales'].median())

# summarizing dates.........................................
# Print the maximum of the date column.
# Print the minimum of the date column.

# Print the maximum of the date column
print(sales['date'].max())

# Print the minimum of the date column
print(sales['date'].min())


# Use the custom iqr function defined for you along with .agg() to print the IQR of the temperature_c column of sales.
# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
    
# Print IQR of the temperature_c column
print(sales['temperature_c'].agg(iqr))

# Update the column selection to use the custom iqr function with .agg() to print the IQR of temperature_c, fuel_price_usd_per_l, and unemployment, in that order.


# Update the aggregation functions called by .agg(): include iqr and np.median in that order.

# Dealing with missing data...................................................................................
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
# Count the number of missing values in each column
print(planes.isna().sum())

# Find the five percent threshold
threshold = len(planes) * 0.05

# Create a filter
cols_to_drop = planes.columns[planes.isna().sum() <= threshold]

# Drop missing values for columns below the threshold
planes.dropna(subset=cols_to_drop, inplace=True)

print(planes.isna().sum())

# Strategies for remaining missing data..........................................................................
# Print the values and frequencies of "Additional_Info".
# Check the values of the Additional_Info column
print(planes["Additional_Info"].value_counts())

# Create a boxplot of "Price" by "Airline"
# Check the values of the Additional_Info column
print(planes["Additional_Info"].value_counts())

# Create a box plot of Price by Airline
sns.boxplot(data=planes, x="Airline", y="Price")

plt.show()


# Group planes by airline and calculate the median price.
# Calculate median plane ticket prices by Airline
airline_prices = planes.groupby("Airline")["Price"].median()

print(airline_prices)

# Convert the grouped median prices to a dictionary.
# Calculate median plane ticket prices by Airline
airline_prices = planes.groupby("Airline")["Price"].median()

print(airline_prices)

# Convert to a dictionary
prices_dict = airline_prices.to_dict()

# Conditionally impute missing values for "Price" by mapping values in the "Airline column" based on prices_dict.
# Check for remaining missing values.
# Calculate median plane ticket prices by Airline
airline_prices = planes.groupby("Airline")["Price"].median()

print(airline_prices)

# Convert to a dictionary
prices_dict = airline_prices.to_dict()

# Map the dictionary to missing values of Price by Airline
planes["Price"] = planes["Price"].fillna(planes["Airline"].map(prices_dict))

# Check for missing values
print(planes.isna().sum())

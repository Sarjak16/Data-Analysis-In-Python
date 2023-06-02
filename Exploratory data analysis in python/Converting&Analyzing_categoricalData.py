# Filter planes for columns that are of "object" data type.
# Loop through the columns in the dataset.
# Add the column iterator to the print statement, then call the function to return the number of unique values in the column.
# Create a list of categories
flight_categories = ["Short-haul", "Medium", "Long-haul"]

# Create conditions, a list containing subsets of planes["Duration"] based on short_flights, medium_flights, and long_flights.
# Create the "Duration_Category" column by calling a function that accepts your conditions list and flight_categories, setting values not found to "Extreme duration".
# Create a plot showing the count of each category.
# Create conditions for values in flight_categories to be created
conditions = [
    (planes["Duration"].str.contains(short_flights)),
    (planes["Duration"].str.contains(medium_flights)),
    (planes["Duration"].str.contains(long_flights))
]

# Apply the conditions list to the flight_categories
planes["Duration_Category"] = np.select(conditions, 
                                        flight_categories,
                                        default="Extreme duration")

# Plot the counts of each category
sns.countplot(data=planes, x="Duration_Category")
plt.show()

#setting and removing indexes..................................................................................................................

# Look at temperatures.
# Set the index of temperatures to "city", assigning to temperatures_ind.
# Look at temperatures_ind. How is it different from temperatures?
# Reset the index of temperatures_ind, keeping its contents.
# Reset the index of temperatures_ind, dropping its contents.


# Look at temperatures
print(temperatures)

# Set the index of temperatures to city
temperatures_ind = temperatures.set_index("city")

# Look at temperatures_ind
print(temperatures_ind.head())

# Reset the temperatures_ind index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the temperatures_ind index, dropping its contents
# print(temperatures_ind.reset_index(drop= True))

# Subsetting with .loc[]........................................................................................................................................
# The killer feature for indexes is .loc[]: a subsetting method that accepts index values. When you pass it a single argument, it will take a subset of rows.

# The code for subsetting using .loc[] can be easier to read than standard square bracket subsetting, which can make your code less burdensome to maintain.

# pandas is loaded as pd. temperatures and temperatures_ind are available; the latter is indexed by city.

# Create a list called cities that contains "Moscow" and "Saint Petersburg".
# Use [] subsetting to filter temperatures for rows where the city column takes a value in the cities list.
# Use .loc[] subsetting to filter temperatures_ind for rows where the city is in the cities list.

# Make a list of cities to subset on
cities = ["Moscow", "Saint Petersburg"]

# Subset temperatures using square brackets
print(temperatures[temperatures["city"].isin(cities)])

# Subset temperatures_ind using .loc[]
print(temperatures_ind.loc[cities])


# Setting multi-level indexes...........................................................................................................................
# Set the index of temperatures to the "country" and "city" columns, and assign this to temperatures_ind.
# Specify two country/city pairs to keep: "Brazil"/"Rio De Janeiro" and "Pakistan"/"Lahore", assigning to rows_to_keep.
# Print and subset temperatures_ind for rows_to_keep using .loc[]

# Index temperatures by country & city
temperatures_ind = temperatures.set_index(["country", "city"])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [("Brazil", "Rio De Janeiro"), ( "Pakistan", "Lahore")]

# Subset for rows to keep
print(temperatures_ind.loc[rows_to_keep])


# Sorting by index values.....................................................................................................................................
# Previously, you changed the order of the rows in a DataFrame by calling .sort_values(). It's also useful to be able to sort by elements in the index. 
# For this, you need to use .sort_index().

# pandas is loaded as pd. temperatures_ind has a multi-level index of country and city, and is available.

# Sort temperatures_ind by the index values.
# Sort temperatures_ind by the index values at the "city" level.
# Sort temperatures_ind by ascending country then descending city.

# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level= "city"))

# Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(level= ["country", "city"], ascending= [True, False]))

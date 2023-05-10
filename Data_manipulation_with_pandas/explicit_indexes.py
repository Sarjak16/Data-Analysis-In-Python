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


# Slicing index values......................................................................................................................................
# Slicing lets you select consecutive elements of an object using first:last syntax. DataFrames can be sliced by index values or by row/column number;
#   we'll start with the first case. This involves slicing inside the .loc[] method.

# Compared to slicing lists, there are a few things to remember.

# You can only slice an index if the index is sorted (using .sort_index()).
# To slice at the outer level, first and last can be strings.
# To slice at inner levels, first and last should be tuples.
# If you pass a single slice to .loc[], it will slice the rows.
# pandas is loaded as pd. temperatures_ind has country and city in the index, and is available.

# Sort the index of temperatures_ind.
# Use slicing with .loc[] to get these subsets:
#  from Pakistan to Russia.
#  from Lahore to Moscow. (This will return nonsense.)
#  from Pakistan, Lahore to Russia, Moscow.

# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Subset rows from Pakistan to Russia
print(temperatures_srt.loc["Pakistan":"Russia"])

# Try to subset rows from Lahore to Moscow
print(temperatures_srt.loc["Lahore":"Moscow"])

# Subset rows from Pakistan, Lahore to Russia, Moscow
print(temperatures_srt.loc[("Pakistan", "Lahore"):("Russia", "Moscow")])


# Slicing in both directions....................................................................................................
# Use .loc[] slicing to subset rows from India, Hyderabad to Iraq, Baghdad.
# Use .loc[] slicing to subset columns from date to avg_temp_c.
# Slice in both directions at once from Hyderabad to Baghdad, and date to avg_temp_c.


# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[("India","Hyderabad"):("Iraq", "Baghdad")])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:,"date":"avg_temp_c"])

# Subset in both directions at once
print(temperatures_srt.loc[('India', 'Hyderabad'):('Iraq', 'Baghdad'), 'date':'avg_temp_c'])


# Slicing time series...............................................................................................................................................
# Slicing is particularly useful for time series since it's a common thing to want to filter for data within a date range. Add the date column to the index, then use .loc[] to perform the subsetting.
# The important thing to remember is to keep your dates in ISO 8601 format, that is, "yyyy-mm-dd" for year-month-day, "yyyy-mm" for year-month, and "yyyy" for year.

# Recall from Chapter 1 that you can combine multiple Boolean conditions using logical operators, such as &. To do so in one line of code, you'll need to add parentheses () around each condition.

# pandas is loaded as pd and temperatures, with no index, is available.

# Use Boolean conditions, not .isin() or .loc[], and the full date "yyyy-mm-dd", to subset temperatures for rows in 2010 and 2011 and print the results.
# Set the index of temperatures to the date column and sort it.
# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011.
# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011

# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = temperatures[(temperatures["date"] >= '2010-1-1') & (temperatures["date"] <= '2011-12-31')]
print(temperatures_bool)

# Set date as the index and sort the index
temperatures_ind = temperatures.set_index("date").sort_index()

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc['2010' : '2011'])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc['2010-8' : '2011-2'])
